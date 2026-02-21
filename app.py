import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configuração de Segurança dos Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Erro: A chave GEMINI_API_KEY não foi configurada nos Secrets!")

st.set_page_config(page_title="Analista Profit Pro", layout="centered")
st.title("📊 Analisador de Setup - Mini Índice")

uploaded_file = st.file_uploader("Suba o print do seu Profit Pro", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gráfico Carregado', use_container_width=True)
    
    if st.button('Analisar Agora'):
        try:
            # MODELO AJUSTADO: Usando gemini-1.5-pro para suporte multimodal
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            prompt = """
            Analise esta imagem do Profit Pro com o setup Gemini/APForce:
            1. Verifique a Regra de Coloração 'Disciplina'.
            2. Olhe o Histograma MACD e o APForceTrend.
            3. Localize o preço em relação ao Pivot.
            Dê um veredito técnico: COMPRA, VENDA ou AGUARDAR.
            """
            
            response = model.generate_content([prompt, image])
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Erro técnico: {e}")
