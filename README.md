# 📄💬 Chat com PDF + Claude 3 Sonnet

Este projeto permite que você faça perguntas sobre o conteúdo de um arquivo PDF utilizando inteligência artificial (Claude 3 Sonnet via OpenRouter). A aplicação é construída em Python com Streamlit e realiza o upload, leitura, chunking e consulta ao modelo de IA, retornando respostas contextuais baseadas no documento enviado.

## Funcionalidades

- Upload de arquivos PDF.
- Extração automática do texto do PDF.
- Divisão do texto em chunks para melhor contexto.
- Interface para perguntas sobre o conteúdo do PDF.
- Respostas geradas por IA (Claude 3 Sonnet via OpenRouter).

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure sua chave de API do OpenRouter:**
   - Crie uma conta em [OpenRouter](https://openrouter.ai/).
   - Obtenha sua chave de API.
   - Defina a variável de ambiente `OPENROUTER_API_KEY`:
     ```bash
     export OPENROUTER_API_KEY="sk-..."
     ```
     Ou edite diretamente no código, se preferir.

4. **Execute a aplicação:**
   ```bash
   streamlit run langlang.py
   ```

5. **Acesse no navegador:**
   - Normalmente em [http://localhost:8501](http://localhost:8501)

## Exemplo de uso

1. Faça upload de um PDF.
2. Digite uma pergunta sobre o conteúdo do PDF.
3. Veja a resposta gerada pela IA baseada no documento.

## Requisitos

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [tiktoken](https://pypi.org/project/tiktoken/)
- [openai](https://pypi.org/project/openai/)

## Observações

- O chunking é feito por tokens para evitar exceder o limite do modelo.
- O modelo utilizado é o `anthropic/claude-3-sonnet` via OpenRouter.
- O código pode ser facilmente adaptado para outros modelos ou provedores.

## Licença

MIT

---

Desenvolvido por
