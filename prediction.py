import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
@st.cache_resource
def load_model():
    return joblib.load("random_forest_model.pkl")

model = load_model()

def prediction_page():
    # Título de la aplicación
    st.title("Predicción de Riesgo de Esclerosis Múltiple")
    st.write("""
    ### Introduce los datos del paciente para predecir si desarrollará Esclerosis Múltiple
    """)

    # Crear el formulario de entrada de datos
    gender = st.radio("Género", options=["Male", "Female"])
    age = st.number_input("Edad", min_value=1, max_value=100, value=30)
    schooling = st.number_input("Años de escolarización", min_value=0, max_value=30, value=12)
    breastfeeding = st.radio("Lactancia materna", options=["Yes", "No", "Unknown"])
    varicella = st.radio("Varicela", options=["Yes", "No"])
    initial_symptom = st.number_input("Síntoma inicial (número)", min_value=0, max_value=20, value=1)
    mono_poly = st.radio("Síntomas (Mono/Polisintomático)", options=["Monosymptomatic", "Polysymptomatic"])
    oligoclonal = st.radio("Bandas oligoclonales", options=["Absent", "Present"])
    llssep = st.selectbox("LLSSEP", options=[0, 1])
    ulssep = st.selectbox("ULSSEP", options=[0, 1])
    vep = st.selectbox("VEP", options=[0, 1])
    baep = st.selectbox("BAEP", options=[0, 1])
    periventricular_mri = st.selectbox("Periventricular MRI", options=[0, 1])
    cortical_mri = st.selectbox("Cortical MRI", options=[0, 1])
    infratentorial_mri = st.selectbox("Infratentorial MRI", options=[0, 1])
    spinal_cord_mri = st.selectbox("Spinal Cord MRI", options=[0, 1])
    initial_edss = st.number_input("Initial EDSS (score)", min_value=0.0, max_value=10.0, value=1.0)
    

    # Botón para realizar la predicción
    if st.button("Predecir"):
        # Convertir los datos a un DataFrame
        data = pd.DataFrame({
            "Gender": [1 if gender == "Male" else 2],
            "Age": [age],
            "Schooling": [schooling],
            "Breastfeeding": [1 if breastfeeding == "Yes" else 2 if breastfeeding == "No" else 3],
            "Varicella": [1 if varicella == "Yes" else 2],
            "Initial_Symptom": [initial_symptom],
            "Mono_or_Polysymptomatic": [1 if mono_poly == "Monosymptomatic" else 2],
            "Oligoclonal_Bands": [0 if oligoclonal == "Absent" else 1],
            "LLSSEP": [llssep],
            "ULSSEP": [ulssep],
            "VEP": [vep],
            "BAEP": [baep],
            "Periventricular_MRI": [periventricular_mri],
            "Cortical_MRI": [cortical_mri],
            "Infratentorial_MRI": [infratentorial_mri],
            "Spinal_Cord_MRI": [spinal_cord_mri],
            "Initial_EDSS": [initial_edss]
        })

        # Realizar la predicción
        prediction = model.predict(data)

        # Mostrar el resultado
        if prediction[0] == 1:
            st.error("El modelo predice que el paciente DESARROLLARÁ esclerosis múltiple.")
        else:
            st.success("El modelo predice que el paciente NO desarrollará esclerosis múltiple.")
