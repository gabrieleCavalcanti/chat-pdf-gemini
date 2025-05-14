import sys
import os
import streamlit as st

# Adiciona caminho para importar módulos do diretório pai
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

# Configuração da página
st.set_page_config(
    page_title="Chat da Gabi com Gemini 🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
    <style>
        body {
            background-color: #f9f9fc;
            font-family: 'Segoe UI', sans-serif;
        }

        .container {
            max-width: 960px;
            margin: auto;
            padding: 20px;
        }

        .titulo {
            font-size: 48px;
            color: #1E3A8A;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .subtitulo {
            font-size: 20px;
            color: #4B5563;
            margin-bottom: 30px;
        }

        .chatbox {
            background: linear-gradient(to right, #e0e7ff, #f3f4f6);
            padding: 25px;
            border-left: 5px solid #4F46E5;
            border-radius: 10px;
            font-size: 18px;
            color: #111827;
            margin-bottom: 20px;
        }

        .resposta {
            background-color: #ffffff;
            padding: 20px;
            border-left: 5px solid #10b981;
            border-radius: 10px;
            font-size: 18px;
            color: #111827;
            margin-top: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        }

        .footer {
            margin-top: 50px;
            font-size: 14px;
            text-align: center;
            color: #9CA3AF;
        }

        .stTextInput > div > input {
            background-color: #f3f4f6;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #d1d5db;
        }

        .stFileUploader {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout da aplicação
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="titulo">🤖 Minha IA com Gemini</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Faça upload de um PDF e tire dúvidas sobre ele!</div>', unsafe_allow_html=True)

st.markdown('<div class="chatbox">Como posso te ajudar hoje?</div>', unsafe_allow_html=True)

# Upload do PDF
uploaded_file = st.file_uploader("📄 Faça upload de um arquivo PDF", type={"pdf"})

# Processamento do PDF
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.session_state["context"] = text
    st.success("✅ PDF carregado e processado com sucesso!")

# Campo de pergunta
question = st.text_input("💬 Digite uma pergunta")

# Resposta da IA
if question and "context" in st.session_state:
    response = ask_gemini(question, st.session_state["context"])
    st.markdown(f'<div class="resposta"><strong>Resposta:</strong><br>{response}</div>', unsafe_allow_html=True)

# Rodapé
st.markdown('<div class="footer">Desenvolvido com 💙 por Gabi</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
