import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configuração limpa
st.set_page_config(page_title="Analista Profit Pro", layout="centered")

# Busca a chave nos Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Configure GEMINI_API_KEY nos Secrets do Streamlit.")
else:
    genai.configure(api_key=api_key)

st.title("📊 Analisador de Setup - Mini Índice")

uploaded_file = st.file_uploader("Suba o print do seu Profit Pro", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico Carregado")

    if st.button("Analisar Setup"):
        try:
            # TENTATIVA COM O MODELO PRO (MAIS ESTÁVEL PARA VISÃO)
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            prompt = "Analise o MACD, Disciplina e APForceTrend. Dê o veredito: COMPRA, VENDA ou AGUARDAR."
            
            response = model.generate_content([prompt, image])
            st.success(response.text)
            
        except Exception:
            try:
                # SE O PRO FALHAR, TENTA O FLASH COM CAMINHO COMPLETO
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                response = model.generate_content([prompt, image])
                st.success(response.text)
            except Exception as e:
                st.error(f"Erro persistente na API: {e}")
                st.info("Dica: Verifique se sua chave no AI Studio tem permissão para 'Gemini 1.5 Flash'.")
