import os
import streamlit as st
from PyPDF2 import PdfReader
import tiktoken
from openai import OpenAI

# Configuração da API do OpenRouter (Claude)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY", "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"),
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(page_title="IA com PDF (Claude)", layout="wide")
st.title("📄💬 Chat com PDF + Claude 3 Sonnet")

# Upload do PDF
uploaded_file = st.file_uploader("📎 Envie um PDF para análise", type="pdf")

# Extrair texto do PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Dividir texto em chunks por tokens
def chunk_text(text, max_tokens=1000):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")  # ainda serve para estimar tokens
    words = text.split()
    chunks = []
    chunk = ""
    for word in words:
        if len(enc.encode(chunk + " " + word)) <= max_tokens:
            chunk += " " + word
        else:
            chunks.append(chunk.strip())
            chunk = word
    chunks.append(chunk.strip())
    return chunks

# Processamento principal
if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(pdf_text)

    st.success("✅ PDF carregado com sucesso!")

    question = st.text_input("❓ Digite sua pergunta sobre o PDF:")

    if question:
        with st.spinner("🧠 Pensando com Claude..."):
            context = "\n\n".join(chunks[:3])  # Pode ajustar para mais chunks se necessário
            prompt = f"""
Você é um assistente jurídico e deve responder com base neste documento:

{context}

Pergunta: {question}
"""

            try:
                response = client.chat.completions.create(
                    model="anthropic/claude-3-sonnet",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5,
                    max_tokens=800  # Reduzido para evitar erro de quota
                )

                st.markdown("### 💬 Resposta:")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Erro ao consultar a IA: {e}")
