import pdfplumber

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        complete_text = ''
        for page in pdf.pages:
            complete_text += page.extract_text()

    return complete_text