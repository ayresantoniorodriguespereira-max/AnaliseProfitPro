# 📊 AnaliseProfitPro - Analisador de Setup Gemini/APForce

Aplicação Streamlit para análise inteligente de setups de trading Gemini/APForce usando a IA Google Gemini (Vision).

## 🚀 Características

- **Análise com IA**: Utiliza o modelo Gemini 1.5 Flash para análise visual de setups
- **Interface Amigável**: Aplicação Streamlit simples e intuitiva
- **Análise Completa**: Verifica:
  - Regra de Coloração 'Disciplina' (Verde/Vermelho)
  - Histograma MACD (acima/abaixo da linha zero)
  - Posição do preço em relação à linha amarela (Robo14i/Pivot)
  - APForceTrend (volume/agressão)
- **Veredito Claro**: Retorna recomendação de COMPRA, VENDA ou AGUARDAR

## 📋 Pré-requisitos

- Python 3.8+
- Conta Google Cloud com acesso à API Gemini
- Chave de API configurada

## 🔧 Instalação

### 1. Clonar o repositório
```bash
git clone <seu-repositorio>
cd AnaliseProfitPro
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar chave de API

#### Opção A: Arquivo `.env` (Desenvolvimento Local)
```bash
cp .env.example .env
# Edite .env e adicione sua chave de API
GEMINI_API_KEY=seu_api_key_aqui
```

#### Opção B: Secrets do Streamlit (Produção)
Crie `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "seu_api_key_aqui"
```

## ▶️ Como Executar

```bash
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`

## 📸 Como Usar

1. **Carregar Print**: Clique em "Escolha o print da tela..." e selecione a imagem do Profit Pro
2. **Visualizar Imagem**: Confirme que a imagem foi carregada corretamente
3. **Analisar**: Clique no botão "Analisar Setup"
4. **Resultado**: Veja o veredito técnico fornecido pela IA

## 🔐 Segurança

- **Nunca commite a chave de API**: A chave está no `.gitignore`
- **Use variáveis de ambiente**: Recomendado para produção
- **Respeite os limites da API**: Fique atento às cotas da Google Cloud

## ⚠️ Aviso Legal

Esta aplicação é apenas para fins educacionais e informativos. As análises fornecidas pela IA são sugestões baseadas em padrões visuais. **Sempre confirme com sua própria análise técnica antes de operar no mercado real.**

## 🛠️ Dependências

- **streamlit**: Framework web para Python
- **Pillow**: Manipulação de imagens
- **google-generativeai**: SDK da API Google Gemini
- **python-dotenv**: Carregamento de variáveis de ambiente

## 📝 Estrutura do Projeto

```
AnaliseProfitPro/
├── app.py                 # Aplicação principal Streamlit
├── requirements.txt       # Dependências do projeto
├── .env.example          # Exemplo de configuração
├── .gitignore            # Arquivos ignorados no Git
└── README.md             # Este arquivo
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📄 Licença

[Defina sua licença aqui]

## 👨‍💻 Autor

[Seu nome/organização]

## 📞 Suporte

Para dúvidas ou suporte, abra uma issue no repositório.

---

**Última atualização**: Fevereiro de 2026