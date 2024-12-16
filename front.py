import streamlit as st

# Funciones para diferentes vistas
def home():
    st.title("Página Principal")
    st.write("Bienvenido a la página principal de la aplicación.")

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
page = st.sidebar.radio("Ir a", ["Página Principal", "Acerca de", "Contacto"])

# Mostrar la vista seleccionada
if page == "Página Principal":
    home()
elif page == "Acerca de":
    about()
elif page == "Contacto":
    contact()

