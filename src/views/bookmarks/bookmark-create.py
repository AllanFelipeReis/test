import streamlit as st
from controllers.bookmarks import add_bookmark
from controllers.schools import list_schools
from datetime import date

st.title("Gerenciamento de Bookmarks")
st.subheader("Criação de Bookmark")



# Formulário para adicionar usuário
with st.form("add_user_form"):
    name = st.text_input("Nome do Usuário")
    email = st.text_input("E-mail do Usuário")
    birthday = st.date_input("Data de Nascimento", min_value=date(1900, 1, 1), max_value=date.today())
    is_adm = st.checkbox("Administrador?")
    password = st.text_input("Senha", type="password")
    submitted = st.form_submit_button("Adicionar Usuário")
    
    if submitted and name and email and password:
        add_bookmark(name, email, password, is_adm=is_adm, birthday=birthday)
        st.success("Usuário adicionado com sucesso!")