from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Load the dataset
file_path = 'conversion_predictors_of_clinically_isolated_syndrome_to_multiple_sclerosis.txt.csv'
df = pd.read_csv(file_path)

# Drop 'id' column as it is not useful
df = df.drop(columns=["id", "Final_EDSS"])

# Separar características y variable objetivo
X = df.drop(columns=["group"])  # Características (excluir variable objetivo)
y = df["group"]  # Variable objetivo

# Dividir el dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

joblib.dump(model, "random_forest_model.pkl")
print("Modelo guardado correctamente.")