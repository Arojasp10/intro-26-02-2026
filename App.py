import streamlit as st
from PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio va un texto largo")
st.write("Reazlizar algo de backend y frondend")
image = Image.open("FondoObsidian.png")
st.image(image, caption="Fondo Obsidian") 

texto = st.text_input("Escriba algo", "Este es el texto")
st.write("El texto escrito es", texto)

st.subheader("ahora dos col")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la 1era columna")
  st.write("Algo de las interfaces")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")

