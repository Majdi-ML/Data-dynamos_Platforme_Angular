import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Charger les données
administration_data = pd.read_excel(r'C:\Users\lando\Desktop\analyse pi\administration_data.xlsx')
emp_data = pd.read_excel(r'C:\Users\lando\Desktop\analyse pi\emp_data.xlsx')

# Supprimer les colonnes inutiles
administration_data.drop(columns=['REGISTRATION_NUMBER', 'DEP_ID'], inplace=True)
emp_data.drop(columns=['REGISTRATION_NUMBER', 'DEP_ID', 'ID_TRAINING', 'ACTIVITY', 'ADRESSE_MISSION', 'LEAVE_TYPE', 'SOURCE_of_employment'], inplace=True)

# Supprimer les espaces blancs supplémentaires dans les adresses
administration_data['ADDRESS'] = administration_data['ADDRESS'].str.strip()
emp_data['ADRESS'] = emp_data['ADRESS'].str.strip()

# Convertir les dates en type datetime
administration_data['STARTING_DATE'] = pd.to_datetime(administration_data['STARTING_DATE'])
administration_data['CONTRACT_START'] = pd.to_datetime(administration_data['CONTRACT_START'])
emp_data['STARTING_DATE'] = pd.to_datetime(emp_data['STARTING_DATE'])
emp_data['CONTRACT_START'] = pd.to_datetime(emp_data['CONTRACT_START'])

# Renommer les colonnes 'CONTRACT_END' si nécessaire
emp_data.rename(columns={'CONTRACT_END': 'CONTRACT_END_emp'}, inplace=True)

# Fusionner les données sur la colonne appropriée
merged_data = pd.merge(administration_data, emp_data, left_on='ID_Employee', right_on='CODE', suffixes=('_admin', '_emp'))

# Vérifier si la colonne 'CONTRACT_END' existe dans les données fusionnées
if 'CONTRACT_END' not in merged_data.columns:
    print("La colonne 'CONTRACT_END' n'existe pas dans les données fusionnées.")
else:
    # Créer une colonne pour indiquer les employés actifs
    merged_data['ACTIVE_EMPLOYEE'] = merged_data['CONTRACT_END'].isnull() | (merged_data['CONTRACT_END'] > pd.to_datetime('now'))

    # Encoder les variables catégorielles
    label_encoders = {}
    for column in merged_data.select_dtypes(include=['object']).columns:
        label_encoders[column] = LabelEncoder()
        merged_data[column] = label_encoders[column].fit_transform(merged_data[column].astype(str))

    # Diviser les données en ensemble d'entraînement et ensemble de test
    X = merged_data.drop(columns=['ACTIVE_EMPLOYEE', 'ID_Employee', 'CODE', 'NAME_EMP_admin', 'NAME_EMP_emp'])
    y = merged_data['ACTIVE_EMPLOYEE']
    if len(X) > 0:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Entraîner le modèle de régression logistique
        if len(X_train) > 0:
            model = LogisticRegression()
            model.fit(X_train, y_train)

            # Prédire les départs anticipés sur l'ensemble de test
            y_pred = model.predict(X_test)

            # Calculer l'accuracy
            accuracy = accuracy_score(y_test, y_pred)
            print("Accuracy:", accuracy)

            # Prédire les départs anticipés pour l'ensemble complet des données
            merged_data['PRED_ACTIVE_EMPLOYEE'] = model.predict(X)

            # Sélectionner les employés suspects de départs anticipés
            suspect_employees = merged_data[merged_data['PRED_ACTIVE_EMPLOYEE'] == 1]

            # Enregistrer les employés suspects dans un fichier Excel
            suspect_employees.to_excel(r'C:\Users\lando\Desktop\analyse pi\suspect_employees.xlsx', index=False)
        else:
            print("Impossible d'entraîner le modèle car l'ensemble d'entraînement est vide.")
    else:
        print("Les données sont trop petites pour être divisées en ensembles d'entraînement et de test.")
