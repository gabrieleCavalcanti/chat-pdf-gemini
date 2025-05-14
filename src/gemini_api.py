import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Erro: A variável GEMINI_API_KEY não foi encontrada. Verifique o arquivo .env")

genai.configure(api_key=api_key)

def ask_gemini(question, context):
    """
    Envia uma pergunta para a API do Gemini usando o contexto do PDF.

    Parameters:
    - question (str): Pergunta do usuário.
    - context (str): Texto extraído do PDF.

    Returns:
    - str: Resposta do modelo.
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Baseado neste documento:\n\n{context}\n\nResponda: {question}")
    return response.text
