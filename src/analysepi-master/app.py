from flask import Flask, render_template, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/profiling": {"origins": "http://localhost:4200"}})

# Charger les données des employés actuels et des candidats externes
current_employees = pd.read_excel(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\emp_data.xlsx")
external_candidates_cv = pd.read_csv(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\cv\cv_data.csv")
external_candidates_linkedin = pd.read_csv(r"C:\Users\majdi\Downloads\bi-data\Data-dynamos_Platforme_Angular-versionf\src\analysepi-master\donnees_employes_organisees.csv")

# Concaténer les données des CV et des profils LinkedIn des candidats
all_candidates = pd.concat([external_candidates_cv, external_candidates_linkedin], ignore_index=True)

# Remplacer les valeurs NaN dans la colonne "Skills" par une liste vide
all_candidates['Skills'] = all_candidates['Skills'].fillna('')

# Définir une liste de compétences pertinentes pour le poste
software_skills = ['Python', 'Java', 'SQL', 'Mysql', 'AZURE', 'Linux', 'Angular', 'Git', 'JavaScript', 'Docker',
                   'C++', 'C#', 'Ruby', 'HTML', 'CSS', 'React', 'Node.js', 'MongoDB', 'AWS', 'RESTful API']

telecom_skills = ['Telecom', 'Network', '5G', 'LTE', 'Fiber Optics', 'RF', 'Wireless', 'VoIP', 'Routing', 'Switching',
                  'SDN', 'NFV', 'DWDM', 'SONET', 'VoLTE', 'IMS', 'TCP/IP', 'IPv6', 'Network Security', 'BGP']

# Fonction pour extraire les compétences pertinentes d'un texte
def extract_skills(text, relevant_skills):
    skills = []
    for skill in relevant_skills:
        if skill.lower() in str(text).lower():
            skills.append(skill)
    return skills

# Ajouter une colonne pour les compétences extraites des CV et des profils LinkedIn des candidats
all_candidates['Software_Skills'] = all_candidates['Skills'].apply(lambda x: extract_skills(x, software_skills))
all_candidates['Telecom_Skills'] = all_candidates['Skills'].apply(lambda x: extract_skills(x, telecom_skills))

# Créer une représentation TF-IDF des compétences pour le département des logiciels
tfidf_vectorizer_software = TfidfVectorizer()
tfidf_matrix_software = tfidf_vectorizer_software.fit_transform(all_candidates['Software_Skills'].apply(lambda x: ' '.join(x)))

# Créer une représentation TF-IDF des compétences pour le département des télécommunications
tfidf_vectorizer_telecom = TfidfVectorizer()
tfidf_matrix_telecom = tfidf_vectorizer_telecom.fit_transform(all_candidates['Telecom_Skills'].apply(lambda x: ' '.join(x)))

# Calculer les similarités cosinus pour le département des logiciels
cosine_similarities_software = cosine_similarity(tfidf_matrix_software, tfidf_matrix_software)
mean_similarities_software = cosine_similarities_software.mean(axis=1)

# Calculer les similarités cosinus pour le département des télécommunications
cosine_similarities_telecom = cosine_similarity(tfidf_matrix_telecom, tfidf_matrix_telecom)
mean_similarities_telecom = cosine_similarities_telecom.mean(axis=1)

# Ajouter la similarité moyenne comme colonne dans le DataFrame des candidats pour chaque département
all_candidates['Similarity_Software'] = mean_similarities_software
all_candidates['Similarity_Telecom'] = mean_similarities_telecom

@app.route('/')
def home():
    return render_template('profiling.component.html')

@app.route('/profiling', methods=['POST'])
def predict():
    try:
        # Sélectionner les 3 meilleurs candidats pour le département des logiciels
        top_software_candidates = all_candidates.nlargest(3, ['Similarity_Software'])
        # Remplacer les valeurs NaN par des chaînes vides dans les DataFrames
        top_software_candidates = top_software_candidates.fillna('')

        # Sélectionner les 3 meilleurs candidats pour le département des télécommunications
        top_telecom_candidates = all_candidates.nlargest(3, ['Similarity_Telecom'])
        # Remplacer les valeurs NaN par des chaînes vides dans les DataFrames
        top_telecom_candidates = top_telecom_candidates.fillna('')

        # Convertir les données en JSON et les renvoyer
        return jsonify({
            'software_candidates': top_software_candidates.to_dict(orient='records'),
            'telecom_candidates': top_telecom_candidates.to_dict(orient='records')
        })
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)