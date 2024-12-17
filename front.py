import streamlit as st
from prediction import prediction_page

# Funciones para diferentes vistas
def home():
# Mostrar la imagen
    st.image("imagen_logo.png")

def about():
    st.title("Acerca de")
    st.write("Esta es una aplicación sencilla creada con Streamlit.")
    st.write("Usa el menú lateral para navegar entre páginas.")

def contact():
    st.title("Contacto")
    st.write("¡Gracias por visitarnos! Aquí puedes dejarnos un mensaje.")
    name = st.text_input("Tu nombre:")
    message = st.text_area("Tu mensaje:")
    if st.button("Enviar"):
        st.success("¡Gracias por tu mensaje!")

# Menú de navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Página Principal", "Prediction"])

# Mostrar la vista seleccionada
if page == "Página Principal":
    home()
elif page == "Prediction":
    prediction_page()


