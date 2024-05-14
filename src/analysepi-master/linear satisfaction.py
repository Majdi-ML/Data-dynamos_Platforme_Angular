import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

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

# Diviser les données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# Prétraitement des données
numeric_features = ['tenure', 'avg_hrs_month']
numeric_transformer = SimpleImputer(strategy='mean')

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

# Création du pipeline du modèle avec XGBoost
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', XGBRegressor(random_state=42))])

# Entraînement du modèle
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Évaluer les performances du modèle (MSE)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Sélectionner les mêmes caractéristiques pour les employés
X_employee = emp_data[features]

# Faire des prédictions sur les employés
employee_predictions = model.predict(X_employee)

# Créer une nouvelle colonne dans le DataFrame emp_data pour stocker les prédictions de satisfaction
emp_data['predicted_satisfaction'] = employee_predictions

# Sauvegarder les résultats dans un fichier Excel
emp_data.to_excel(r"C:\Users\lando\Desktop\analyse pi\predictions_satisfaction_employes_xgboost.xlsx", index=False)
