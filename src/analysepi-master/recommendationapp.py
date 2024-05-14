from flask import Flask, request, jsonify, json
from flask_cors import CORS
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
CORS(app, resources={r"/recommendations": {"origins": "http://localhost:4200"}})

# Charger les données et prétraiter si nécessaire
# Charger les données de compétences des employés et de formations Coursera
df_emp_skills = pd.read_excel(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\emp_skills.xlsx")
df_coursera_trainings = pd.read_excel(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\Coursera_trainings-2.xlsx")

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

@app.route("/recommendations", methods=['POST'])
def get_recommendations():
    data = request.json

    # Récupérer les données de recherche depuis la requête POST
    emp_name = data.get('emp_name', '')
    department = data.get('department', '')

    # Filtrer les données en fonction des paramètres de recherche
    filtered_data = df_emp_skills
    if emp_name:
        filtered_data = filtered_data[filtered_data['NAME_EMP'] == emp_name]
    if department:
        filtered_data = filtered_data[filtered_data['DEP_ID'] == department]

    # Générer les recommandations pour les données filtrées
    recommended_courses = []
    for emp_index, emp_row in filtered_data.iterrows():
        emp_skills_similarity = similarity_df.loc[emp_index]

        # Trouver la formation la plus similaire
        recommended_course_index = emp_skills_similarity.idxmax()
        recommended_course_similarity = emp_skills_similarity.max()

        # Obtenir le rating de la formation recommandée
        recommended_course_rating = df_coursera_trainings.loc[recommended_course_index, 'Course Rating']

        # Stocker les informations sur la formation recommandée, y compris le département
        recommended_course = {
            'RecommendedCourse': df_coursera_trainings.loc[recommended_course_index, 'Course Name'],
            'SimilarityScore': recommended_course_similarity,
            'CourseRating': recommended_course_rating,
        }
        recommended_courses.append(recommended_course)

    return jsonify(recommended_courses)

if __name__ == '__main__':
    app.run(debug=True)
