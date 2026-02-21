import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração da chave de API (use variável de ambiente para segurança)
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("❌ Chave de API não encontrada. Configure GEMINI_API_KEY nas variáveis de ambiente ou em st.secrets")
    st.stop()

genai.configure(api_key=api_key)

st.set_page_config(page_title="Analista Gemini - Trader", layout="centered")

st.title("📊 Analisador de Setup Gemini/APForce")
st.write("Arraste ou cole o print do seu Profit Pro abaixo.")

# Upload da imagem
uploaded_file = st.file_uploader("Escolha o print da tela...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada', use_column_width=True)
    
    if st.button('Analisar Setup'):
        with st.spinner('Analisando com IA...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # O "Cérebro" do setup configurado para você
            prompt = """
            Analise esta imagem do Profit Pro com o setup Gemini/APForce:
            1. Verifique a Regra de Coloração 'Disciplina'. Se estiver Verde, é compra. Se Vermelho, é venda.
            2. Olhe o Histograma MACD: Está acima ou abaixo da linha zero?
            3. Localize o preço em relação à linha amarela (Robo14i/Pivot).
            4. Cheque o APForceTrend (volume/agressão).
            Retorne um veredito claro: COMPRA, VENDA ou AGUARDAR, justificando com base nos indicadores visíveis.
            """
            
            response = model.generate_content([prompt, image])
            
            st.subheader("🎯 Veredito Técnico:")
            st.write(response.text)
            
            # Exibe informações adicionais
            st.divider()
            st.caption("⚠️ Aviso: Esta análise é apenas informativa. Sempre confirm com sua própria análise antes de operar.")
