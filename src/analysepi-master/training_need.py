import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Charger les données
df_emp_skills = pd.read_excel(r"C:\Users\lando\Desktop\analyse pi\emp_skills.xlsx")
df_coursera_trainings = pd.read_excel(r"C:\Users\lando\Desktop\analyse pi\Coursera_trainings-2.xlsx")

# Supprimer les lignes avec des valeurs manquantes dans la colonne 'skills'
df_emp_skills = df_emp_skills.dropna(subset=['skills'])

# Créer une représentation vectorielle des compétences des employés
vectorizer = CountVectorizer()
skills_matrix = vectorizer.fit_transform(df_emp_skills['skills'])

# Créer une représentation vectorielle des compétences requises pour les formations
courses_matrix = vectorizer.transform(df_coursera_trainings['Course Name'])

# Calculer la similarité cosinus entre les compétences des employés et les compétences requises pour les formations
similarity_matrix = cosine_similarity(skills_matrix, courses_matrix)

# Créer une DataFrame pour stocker les scores de similarité
similarity_df = pd.DataFrame(similarity_matrix, index=df_emp_skills.index, columns=df_coursera_trainings.index)

# Pour chaque employé, trouver les formations recommandées

   # Pour chaque employé, trouver les formations recommandées
recommended_courses = {}
for emp_index, emp_row in df_emp_skills.iterrows():
    emp_code = emp_row['CODE']
    emp_name = emp_row['NAME_EMP']
    emp_department = emp_row['DEP_ID']  # Ajouter cette ligne pour obtenir le département de l'employé
    emp_skills_similarity = similarity_df.loc[emp_index]
    
    # Trouver la formation la plus similaire
    recommended_course_index = emp_skills_similarity.idxmax()
    recommended_course_similarity = emp_skills_similarity.max()
    
    # Obtenir le rating de la formation recommandée
    recommended_course_rating = df_coursera_trainings.loc[recommended_course_index, 'Course Rating']
    
    # Stocker les informations sur la formation recommandée, y compris le département
    recommended_courses[(emp_code, emp_name)] = {
        'Recommended Course': df_coursera_trainings.loc[recommended_course_index, 'Course Name'],
        'Similarity Score': recommended_course_similarity,
        'Course Rating': recommended_course_rating,
        'Department': emp_department  # Ajouter le département de l'employé
    }

# Afficher les recommandations pour chaque employé, en tenant compte du rating
for emp_id, recommendation in recommended_courses.items():
    emp_code, emp_name = emp_id
    print(f"Pour l'employé avec le code {emp_code}, le nom '{emp_name}', et le département '{recommendation['Department']}', la formation recommandée est '{recommendation['Recommended Course']}' avec un score de similarité de {recommendation['Similarity Score']:.2f} et un rating de {recommendation['Course Rating']}.")

# Enregistrer les recommandations dans un fichier Excel
pd.DataFrame.from_dict(recommended_courses, orient='index').reset_index() \
            .rename(columns={'index': 'Employee', 0: 'Recommendation'}).to_excel(r"C:\Users\lando\Desktop\analyse pi\recommendations.xlsx", index=False)
