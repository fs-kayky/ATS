# 📄 ATS - Sistema de Triagem de Candidatos com IA  

Este projeto é um sistema de triagem automatizado de currículos que utiliza IA para analisar e classificar candidatos com base nos requisitos da vaga. O sistema lê arquivos PDF contendo currículos e descrições de vagas, processa as informações usando IA (Gemini) e gera relatórios detalhados em PDF.

---

## 🚀 Funcionalidades  

✅ Extração de texto de arquivos PDF.  
✅ Análise inteligente dos currículos com IA.  
✅ Comparação dos candidatos com os requisitos da vaga.  
✅ Geração automática de relatórios em PDF.  

---

## 🛠️ Tecnologias Utilizadas  

- **Python**  
- **Google Gemini API**  
- **Tkinter** (para seleção de arquivos)  
- **PyMuPDF** (extração de texto de PDFs)  
- **ReportLab** (geração de PDFs)  
- **python-dotenv** (gerenciamento de variáveis de ambiente)  

---

## 📌 Pré-requisitos  

Antes de começar, instale as dependências necessárias:  

```bash
pip install -r requirements.txt
```

Além disso, crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google Gemini:

```
GEMINI_KEY=SEU_TOKEN_AQUI
```

---

## 📦 Como Usar  

1️⃣ **Execute o programa:**  

```bash
python main.py
```

2️⃣ **Escolha o arquivo PDF da vaga** (o sistema usará este arquivo para extrair os requisitos da posição).  

3️⃣ **Selecione os PDFs dos currículos** (podem ser vários arquivos ao mesmo tempo).  

4️⃣ **Aguarde o processamento pela IA** (ela irá comparar cada candidato com os requisitos da vaga).  

## 📜 Licença  

Este projeto é open-source e está disponível sob a licença MIT.  

---

💡 **Desenvolvido por [Kayky Rodrigues](https://www.linkedin.com/in/fs-kayky/)** 🚀

