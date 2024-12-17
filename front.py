import streamlit as st
from prediction import prediction_page

# Funciones para diferentes vistas
def home():
# Mostrar la imagen
    st.image("imagen_logo.png")

# Menú de navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Página Principal", "Prediction"])

# Mostrar la vista seleccionada
if page == "Página Principal":
    home()
elif page == "Prediction":
    prediction_page()


