import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configuração de Segurança dos Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Erro: A chave GEMINI_API_KEY não foi configurada nos Secrets do Streamlit.")

st.set_page_config(page_title="Analista Profit Pro", layout="centered")

st.title("📊 Analisador de Setup - Mini Índice")
st.write("Suba o print do seu Profit Pro para análise técnica.")

uploaded_file = st.file_uploader("Escolha o print...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gráfico Carregado', use_container_width=True)
    
    if st.button('Analisar Agora'):
        try:
            # Usando a versão estável mais compatível
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            
            prompt = """
            Analise esta imagem do Profit Pro com o setup Gemini/APForce:
            1. Verifique a Regra de Coloração 'Disciplina'. Se estiver Verde, é compra. Se Vermelho, é venda.
            2. Olhe o Histograma MACD: Está acima ou abaixo da linha zero?
            3. Localize o preço em relação à linha amarela (Robo14i/Pivot).
            4. Cheque o APForceTrend (volume/agressão).
            Retorne um veredito claro: COMPRA, VENDA ou AGUARDAR.
            """
            
            response = model.generate_content([prompt, image])
            
            st.subheader("Veredito Técnico:")
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Ocorreu um erro na análise: {e}")
            st.info("Dica: Verifique se sua chave de API no AI Studio está ativa.")
