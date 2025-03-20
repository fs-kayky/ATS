import pdfplumber


def extract_text(pdf_path):
    if not isinstance(pdf_path, str):
        pdf_path.file.seek(0)
        pdf_path = pdf_path.file

    complete_text = ''

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                complete_text += page_text + "\n"

    return complete_text
