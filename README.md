# llama3-pdf-reader
Esse projeto mostra como a interação simples de um modelo LLM com PDFs permite responder perguntas sobre seu conteúdo.   
Esse projeto usa como base dois outros projetos: [AI-Data-Analyzer](https://github.com/danttis/AI-Data-Analyzer/) e [ChatBot-Ollama](https://github.com/danttis/ChatBot-Ollama).

## Funcionalidades:

- **Leitura e exibição de PDFs**: permite visualização do PDfs escolhido.
- **Interação com conteúdo**: É possível fazer perguntas sobre o PDF selecionado e ter respostas imediatas.
- **Interface de Usuário Simples**: Construída com Streamlit, oferecendo uma experiência intuitiva para o usuário.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte configurado:

- Acesso à API do Llama 3, seja localmente ou através de [Groq](https://console.groq.com/docs/quickstart) ou outras alternativas.
- Python 3.10 ou superior.
- Os seguintes pacotes Python devem estar instalados:

  - `streamlit`
  - `streamlit-pdf-viewer`
  - `pymupdf`
  - `groq`

Você pode instalar os pacotes necessários usando o comando:

```bash
pip install streamlit streamlit-pdf-viewer pymupdf groq
```

## Como Usar

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/danttis/llama3-pdf-reader.git
   cd llama3-pdf-reader
   ```
2. **Configure a conexão**

   - Configure a conexão com a API do modelo que deseje usar, no arquivo `api.py`.
     
3. **Execute o Aplicativo**:

   - Inicie o aplicativo Streamlit:

   ```bash
   streamlit run app.py
   ```
4. **Carregue seu PDF**:

   - Use a interface do usuário para carregar o seu PDF e começar a conversar com o modelo sobre seus dados.
  
## Observações:
  - Ao usar, lembre de limitar a quantidade de caracteres do PDF.
