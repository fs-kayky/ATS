import pdfplumber

def extract_text(pdf_path):
    pdf_path.file.seek(0)
    complete_text = ''

    with pdfplumber.open(pdf_path.file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                complete_text += page_text + "\n"

    return complete_text