import streamlit as st
import pymysql
# import mysql.connector

# Conexão ao banco de dados
def get_connection():
    # return mysql.connector.connect(
    #     host=st.secrets.db_credentials.host,
    #     user=st.secrets.db_credentials.user,
    #     password=st.secrets.db_credentials.password,
    #     database=st.secrets.db_credentials.db
    # )
    timeout = 10
    return pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db=st.secrets.db_credentials.db,
        host=st.secrets.db_credentials.host,
        password=st.secrets.db_credentials.password,
        read_timeout=timeout,
        port=16202,
        user=st.secrets.db_credentials.user,
        write_timeout=timeout,
    )