from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/satisfaction": {"origins": "http://localhost:4200"}})

# Fonction pour convertir les salaires en catégories
def categorize_salary(salary):
    try:
        salary = int(salary)  # Convertir la valeur de salaire en entier
        if salary < 1500:
            return 'low'
        elif 1500 <= salary <= 2500:
            return 'medium'
        else:
            return 'high'
    except ValueError:
        return salary

# Charger les données d'entraînement
employee_churn_data = pd.read_csv(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\cv\train model\employee_churn_data.csv")

# Renommer les colonnes de la table emp_data pour correspondre à celles de employee_churn_data
emp_data = pd.read_excel(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\emp_data.xlsx")
emp_data.rename(columns={'SALARY': 'salary', 'HOURS': 'avg_hrs_month', 'TENURE': 'tenure'}, inplace=True)

# Appliquer la fonction de conversion aux salaires dans les données d'entraînement
employee_churn_data['salary'] = employee_churn_data['salary'].apply(categorize_salary)

# Sélectionner les caractéristiques pertinentes pour le modèle
features = ['salary', 'tenure', 'avg_hrs_month']
X_train = employee_churn_data[features]
y_train = employee_churn_data['satisfaction']

# Prétraitement des données
numeric_features = ['tenure', 'avg_hrs_month']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

categorical_features = ['salary']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Création du pipeline du modèle
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Entraînement du modèle
model.fit(X_train, y_train)

@app.route('/satisfaction', methods=['POST'])
def predict():
    try:
        data = request.json

        # Récupérer les données de recherche depuis la requête POST
        emp_name = data.get('emp_name', '')
        department = data.get('department', '')

        # Filtrer les données en fonction des paramètres de recherche
        filtered_data = [
            {
                'NAME_EMP': row['NAME_EMP'],
                'TYPE_DIPLOMA': row['TYPE_DIPLOMA'],
                'EXP_YEARS': row['EXP_YEARS'],
                'GENDER': row['GENDER'],
                'POSITION': row['POSITION'],
                'predicted_satisfaction': model.predict(row[features].values.reshape(1, -1))[0]
            }
            for _, row in emp_data.iterrows()
            if (emp_name == '' or row['NAME_EMP'] == emp_name)
            and (department == '' or row['DEP_ID'] == department)
        ]

        # Retourner les prédictions au format JSON
        return jsonify(predictions=filtered_data)

    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)