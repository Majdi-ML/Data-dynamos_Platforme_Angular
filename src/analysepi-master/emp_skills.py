import pandas as pd

# Charger les données de la table emp_data
df_emp_data = pd.read_excel(r"C:\Users\lando\Desktop\analyse pi\emp_data.xlsx")
# Remplacer les valeurs nulles ou vides dans la colonne ID_TRAINING par une liste vide
df_emp_data['ID_TRAINING'] = df_emp_data['ID_TRAINING'].fillna('').astype(str)

# Fonction pour transformer chaque chaîne en une liste d'identifiants de formation
def process_training_ids(training_ids):
    if training_ids.strip() == "":
        return []
    else:
        # Exclure l'identifiant 3523 lors de la transformation
        return [int(id.strip()) for id in training_ids.strip('[]').split(',') if id.strip() != '3523']

# Appliquer la fonction pour transformer chaque valeur de la colonne ID_TRAINING
df_emp_data['ID_TRAINING'] = df_emp_data['ID_TRAINING'].apply(process_training_ids)

# Charger les données des formations depuis le fichier Coursera_trainings-2.xlsx
df_coursera_trainings = pd.read_excel(r"C:\Users\lando\Desktop\analyse pi\Coursera_trainings-2.xlsx")

# Créer un dictionnaire de correspondance entre les IDs de formation et les noms de formation
id_to_name = dict(zip(df_coursera_trainings['course_id'], df_coursera_trainings['Course Name']))

# Fonction pour récupérer les noms des formations à partir des IDs
def get_skills(ids):
    skills = []
    for id in ids:
        if id in id_to_name:
            skills.append(id_to_name[id])
        else:
            print(f"Identifiant de formation {id} non trouvé.")
    return ', '.join(skills)


# Appliquer la fonction pour obtenir les noms des formations pour chaque employé
df_emp_data['skills'] = df_emp_data['ID_TRAINING'].apply(get_skills)

# Enregistrer le résultat dans un nouveau fichier Excel
df_emp_data.to_excel(r"C:\Users\lando\Desktop\analyse pi\emp_skills.xlsx", index=False)
