import functions.extract_pdf_text as text_extract
import functions.select_pdf as pdf_select
import gemini.gemini_handler as genai


# ENTRY PROGRAM TO GENERATE ATS RESPONSES


def ats_cycle():
    print('Selecione o arquivo "Requerimentos da Vaga"...')
    role_pdf_path = pdf_select.select_pdf()
    requirements_text = text_extract.extract_text(role_pdf_path)

    print('\nEscolha todos os Currículos referentes a essa vaga...')
    resumes_path = pdf_select.select_multiples_pdfs()

    for resume_path in resumes_path:
        resume_text = text_extract.extract_text(resume_path)

        msg = f"""
        Requisitos da vaga:
        {requirements_text}
        
        Currículo do candidato:
        {resume_text}
        """

        ia_response = genai.consult_genai(msg)

        if ia_response:
            print(f"{ia_response}")


if __name__ == "__main__":
    ats_cycle()
