from fastapi import APIRouter, UploadFile, FastAPI, UploadFile, File, HTTPException
import gemini.gemini_handler as genai
from bson import ObjectId
from models.models import Job
from database.database import jobs_collection
from typing import List
import functions.extract_pdf_text as pdf_text
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/jobs")
async def create_job(title: str):
    job = Job(title)
    result = await jobs_collection.insert_one(job.__dict__)
    return {"job_id": str(result.inserted_id)}

@router.post("/jobs/{job_id}/requirements")
async def upload_requirements(job_id: str, file: UploadFile = File(...)):
    text = pdf_text.extract_text(file)
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")

    await jobs_collection.update_one({"_id": ObjectId(job_id)}, {"$set": {"requirements": {"text": text}}})
    return {"message": "Requisitos atualizados com sucesso"}

@router.post("/jobs/{job_id}/candidates")
async def add_candidates(job_id: str, files: List[UploadFile] = File(...)):
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")

    job_requirements = job.get("requirements", "")
    if not job_requirements:
        raise HTTPException(status_code=400, detail="Requisitos da vaga não encontrados")

    candidates = []
    for file in files:
        text = pdf_text.extract_text(file) 
        
        prompt = f"Requisitos da vaga:\n{job_requirements}\n\nCurrículo do candidato:\n{text}"
        candidate_data = genai.consult_genai(prompt)

        if candidate_data:
            candidate = {
                "name": candidate_data["nome_candidato"],
                "match": candidate_data["match_vaga"],
                "score": candidate_data["nota_geral"],
                "strengths": candidate_data["pontos_fortes"],
                "weaknesses": candidate_data["pontos_fracos"],
                "questions": candidate_data["perguntas_modelo"]
            }
            candidates.append(candidate)

    await jobs_collection.update_one(
        {"_id": ObjectId(job_id)},
        {"$push": {"candidates": {"$each": candidates}}}
    )

    return {"message": "Candidatos adicionados", "data": candidates}

@router.get("/jobs/{job_id}/candidates")
async def get_candidates(job_id: str):
    try:
        obj_id = ObjectId(job_id)
    except Exception:
        raise HTTPException(status_code=400, detail="job_id inválido")

    job = await jobs_collection.find_one({"_id": obj_id})
    if not job:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")

    job_serialized = jsonable_encoder(job, custom_encoder={ObjectId: str})

    return job_serialized.get("candidates", [])