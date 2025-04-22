import streamlit as st
import pandas as pd

st.set_page_config(page_title="Painel Nampula RH", layout="wide")

# Cabeçalho
st.title("Painel Nampula RH")
st.subheader("Sistema desenvolvido exclusivamente para Mostafa Carlos João – Nampula, Moçambique")
st.caption("Ver mais longe. Agir com dados. Liderar com propósito.")

# Upload de arquivos
st.sidebar.header("Carregar Dados")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo PDF ou Excel", type=["pdf", "xlsx"])

if uploaded_file:
    st.success("Arquivo recebido com sucesso!")

    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
        st.subheader("Pré-visualização dos dados:")
        st.dataframe(df)

        # Se quiseres colocar lógica de resumo, coloca aqui:
        st.subheader("Área de Constatações, Conclusões, Desafios e Recomendações")
        st.info("Esta seção será automatizada em breve com IA.")
    
    elif uploaded_file.name.endswith(".pdf"):
        st.warning("Leitura de PDF ainda será ativada. Aguarde próxima versão.")

# Rodapé
st.markdown("---")
st.markdown("**© 2025 – Mostafa Carlos João** | Painel Nampula RH | Powered by Streamlit")
