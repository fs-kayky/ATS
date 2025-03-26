import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY") 

genai.configure(api_key=GEMINI_KEY)


def consult_genai(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    full_prompt = f"""
    Você é um assistente ATS. Analise o currículo e os requisitos da vaga e retorne um JSON com:
    - "nome_candidato": Nome Disponivel no curriculo
    - "match_vaga": valor percentual de compatibilidade com a vaga
    - "nota_geral": um número de 0 a 5 indicando a adequação do candidato.
    - "perguntas_modelo": Uma lista de até 5 perguntas que testariam grande parte das habilidades do candidato, para vaga especifica.
    - "pontos_fortes": uma lista de habilidades relevantes do candidato.
    - "pontos_fracos": uma lista de habilidades que faltam.
    Entrada:
    {prompt}
    
    Responda apenas com um JSON sem explicações adicionais.
    """
    print(full_prompt)
    
    response = model.generate_content(full_prompt)
    
    try:
        match = re.search(r"\{.*}", response.text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)
        else:
            raise ValueError("Resposta do Gemini não contém um JSON válido")
    except Exception as e:
        print("GENAI PROCESS ANSWER ERROR:", str(e))
        return None
