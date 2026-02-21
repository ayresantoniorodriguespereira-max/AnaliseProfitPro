import streamlit as st
from PIL import Image
import google.generativeai as genai

# Força a configuração da chave a partir dos Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("ERRO: Configure GEMINI_API_KEY nos Secrets do Streamlit.")

st.title("📊 Analisador de Setup - Mini Índice")

uploaded_file = st.file_uploader("Suba o print do Profit Pro", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico Carregado")

    if st.button("Analisar Setup"):
        try:
            # CHAMADA SIMPLIFICADA PARA EVITAR ERRO 404
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = "Analise o MACD, Disciplina e APForceTrend. Dê o veredito: COMPRA, VENDA ou AGUARDAR."
            
            # Gerando conteúdo com tratamento de erro específico
            response = model.generate_content([prompt, image])
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Erro na comunicação com a IA: {e}")
            st.info("Dica: Se o erro persistir, tente gerar uma nova chave no AI Studio.")
