import pandas as pd
import streamlit as st

URL = "https://docs.google.com/spreadsheets/d/1u1nDgu7gnrh2FsNz5y50DQ_278W2CTbqdmeKLtNsRnQ/edit?usp=sharing"

def consultar_dispositivo(nome_dispositivo):
    df = pd.read_csv(URL)

    # pegar colunas automaticamente
    col_dispositivo = df.columns[2]
    col_nome = df.columns[1]
    col_local = df.columns[3]

    df_filtrado = df[df[col_dispositivo] == nome_dispositivo]

    if df_filtrado.empty:
        return None

    ultimo = df_filtrado.iloc[-1]

    return ultimo[col_nome], ultimo[col_local]

st.title("🔳 Controle de Tablets")

dispositivo = st.selectbox(
    "Selecione o dispositivo:",
    [
        "Tablet 1",
        "Tablet 2",
        "Tablet 3",
        "Tablet 4",
        "Tablet 5",
        "Tablet 6",
        "Tablet 7",
        "Tablet 8",
        "Tablet 9",
        "Tablet 10",
        "Tablet 11",
        "Tablet 12",
        "Tablet 13",
        "Tablet 14",
        "Tablet 15",
        "Tablet 16",
        "Tablet 17",
        "Tablet 18",
        "Tablet 19",
        "Tablet 20",
        "Tablet 21",
        "Tablet 22",
        "Tablet 23",
        "Tablet 24",
        "Tablet 25",
        "Tablet 26",
        "Tablet 27",
        "Tablet 28",
        "Tablet 29",
        "Tablet 30",
        "Tablet 31",
        "Tablet 32"
    ]
)

if st.button("Consultar"):
    resultado = consultar_dispositivo(dispositivo)

    if resultado:
        nome, local = resultado
        st.success(f"Responsável: {nome}")
        st.info(f"Local: {local}")
    else:
        st.warning("Nenhum registro encontrado.")
