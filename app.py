import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from api import generate_code
import fitz  

def main():
    st.set_page_config(
        page_title="PDF Reader",
        page_icon=":rocket:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if 'chat' not in st.session_state:
        st.session_state['chat'] = []

    data_file = st.sidebar.file_uploader("Carregue seu PDF", type=["pdf"])

    if data_file is not None:
        # Salvar o arquivo carregado temporariamente
        with open("uploaded_pdf.pdf", "wb") as f:
            f.write(data_file.getbuffer())

        # Crie duas colunas com proporções iguais
        col1, col2 = st.columns([1, 1])

        # Coloque o visualizador de PDF na coluna 1
        with col1:
            pdf_viewer("uploaded_pdf.pdf")

        # Extrair texto do PDF
        text = ""
        doc = fitz.open("uploaded_pdf.pdf")
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()

        # Adicione o chat na coluna 2
        with col2:
            prompt = st.chat_input('Qual sua dúvida sobre o documento?')

            if prompt:
                st.session_state.chat.append('user: ' + prompt)
                output = generate_code(text, prompt)

                if output:
                    st.session_state.chat.append('model: ' + output)

            if st.session_state.chat:
                for text in st.session_state.chat:
                    if text.startswith('user:'):
                        text = text.replace('user:', '')
                        max_width = min(len(text) * 10, 600)
                        st.markdown(
                            f"""
                            <div style='max-width: {max_width}px; margin-left: auto; margin-bottom: 10px; margin-right: 10px; background-color: #DCF8C6; border-radius: 10px; padding: 10px; text-align: right;'>
                                <p style='font-size: 14px; color: #333333;'>{text}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    elif text.startswith('model:'):
                        text = text.replace('model:', '')
                        max_width = min(len(text) * 10, 600)
                        st.markdown(
                            f"""
                            <div style='max-width: {max_width}px; margin-right: auto; margin-bottom: 10px; margin-left: 10px; background-color: #F0F0F0; border-radius: 10px; padding: 10px; text-align: left;'>
                                <p style='font-size: 14px; color: #000000;'>{text}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

    else:
        st.write("Por favor, carregue um arquivo PDF para visualizar.")

if __name__ == '__main__':
    main()
