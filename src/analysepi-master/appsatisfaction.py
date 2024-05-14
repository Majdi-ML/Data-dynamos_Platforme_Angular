from flask import Flask, request, jsonify
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
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
employee_churn_data = pd.read_csv(r"C:\Users\lando\Desktop\analyse pi\cv\train model\employee_churn_data.csv")

# Renommer les colonnes de la table emp_data pour correspondre à celles de employee_churn_data
emp_data = pd.read_excel(r"C:\Users\lando\Desktop\analyse pi\emp_data.xlsx")
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
        data = request.json  # Récupérer les données JSON de la requête
        X = pd.DataFrame(data)  # Convertir les données en DataFrame
        X_subset = X[['CODE', 'NAME_EMP', 'TYPE_DIPLOMA', 'EXP_YEARS', 'GENDER', 'POSITION', 'predicted_satisfaction']]
        predictions = model.predict(X_subset)  # Faire des prédictions sur les données
        
        # Convertir les prédictions en DataFrame
        predictions_df = pd.DataFrame(predictions, columns=['Predicted_Satisfaction'])
        
        # Enregistrer les prédictions dans un fichier Excel
        file_path = r"C:\Users\lando\Desktop\analyse pi\cv\train model\majdiyaatekasba.xlsx"
        try:
            predictions_df.to_excel(file_path, index=False)
            print("Predictions saved to Excel file:", file_path)
        except Exception as e:
            print("Error saving predictions to Excel file:", e)
        
        return jsonify({'predictions': predictions.tolist()})  # Renvoyer les prédictions sous forme de JSON
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
