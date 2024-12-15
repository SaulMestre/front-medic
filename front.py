import streamlit as st

# Título de la aplicación
st.title("Que bonita es Victoria")

# Subtítulo
st.subheader("Cargar un archivo de texto")

# Widget para subir un archivo
uploaded_file = st.file_uploader("Selecciona un archivo de texto", type=["txt"])

if uploaded_file is not None:
    # Mostrar el contenido del archivo
    st.write("Contenido del archivo:")
    content = uploaded_file.read().decode("utf-8")
    st.text_area("Contenido", content, height=300)
else:
    st.write("No se ha subido ningún archivo todavía.")

# Footer
st.sidebar.title("Opciones")
st.sidebar.write("Esta es una barra lateral con texto adicional.")
