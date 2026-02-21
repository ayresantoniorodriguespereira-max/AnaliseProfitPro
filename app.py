import streamlit as st
import google.generativeai as genai
from PIL import Image

# Tenta configurar a chave
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Configure GEMINI_API_KEY nos Secrets.")

st.title("📊 Analisador de Setup - Mini Índice")

uploaded_file = st.file_uploader("Suba o print do Profit Pro", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Analisar Setup"):
        try:
            # FORÇA O USO DO MODELO SEM PREFIXOS OU SUFIXOS
            # Se o flash falhar, ele tenta o pro automaticamente
            model_name = 'gemini-1.5-flash'
            model = genai.GenerativeModel(model_name)
            
            # Comando direto
            response = model.generate_content([
                "Analise o MACD, Disciplina e APForceTrend. Dê o veredito: COMPRA, VENDA ou AGUARDAR.",
                image
            ])
            st.success(response.text)
            
        except Exception as e:
            # SE O ERRO 404 APARECER, ELE TENTA UMA SEGUNDA OPÇÃO
            try:
                model = genai.GenerativeModel('gemini-1.5-pro')
                response = model.generate_content(["Analise o setup.", image])
                st.success(response.text)
            except Exception as e2:
                st.error(f"Erro persistente: {e2}")
                st.info("Dica técnica: Verifique se sua chave tem faturamento configurado no AI Studio, mesmo no nível gratuito.")
