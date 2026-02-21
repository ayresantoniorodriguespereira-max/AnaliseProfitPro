import streamlit as st
from PIL import Image
import google.generativeai as genai
import google.ai.generativelanguage as glm

# Configuração da Chave
if "GEMINI_API_KEY" in st.secrets:
    # FORÇA O USO DA API v1 (ESTÁVEL) EM VEZ DA v1beta
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='grpc')
else:
    st.error("Configure GEMINI_API_KEY nos Secrets.")

st.title("📊 Analisador de Setup - Mini Índice")

uploaded_file = st.file_uploader("Suba o print do Profit Pro", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gráfico Carregado")

    if st.button("Analisar Setup"):
        try:
            # USA O NOME DIRETO DO MODELO ESTÁVEL
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = "Analise o MACD, Disciplina e APForceTrend. Dê o veredito: COMPRA, VENDA ou AGUARDAR."
            
            response = model.generate_content([prompt, image])
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Erro na comunicação com a IA: {e}")
            st.info("Tente reiniciar o app no painel do Streamlit (Reboot).")
