import tkinter as tk
from tkinter import filedialog

def select_pdf():
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    return pdf_path

def select_multiples_pdfs():
    root = tk.Tk()
    root.withdraw()
    paths_pdf = filedialog.askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
    return paths_pdf