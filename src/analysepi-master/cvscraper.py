import re
import subprocess
import nltk
import docx2txt
from pdfminer.high_level import extract_text
import os
import pandas as pd
import spacy

# Charger le modèle NLP pré-entraîné pour la langue anglaise
nlp = spacy.load("en_core_web_sm")

# Expressions régulières pour la détection des numéros de téléphone et des adresses e-mail
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

# Charger les compétences à partir des fichiers CSV et Excel
skills_csv_df = pd.read_csv(r'C:\Users\lando\Desktop\analyse pi\cv\train model\skills.csv')
skills_excel_df = pd.read_excel(r'C:\Users\lando\Desktop\analyse pi\cv\train model\Technology Skills.xlsx', usecols=['Commodity Title'])

# Fusionner les compétences des deux fichiers
skills_set = set(skills_csv_df['Skill']).union(set(skills_excel_df['Commodity Title']))

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def doc_to_text_catdoc(file_path):
    try:
        process = subprocess.Popen(
            ['catdoc', '-w', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
    except (
        FileNotFoundError,
        ValueError,
        subprocess.TimeoutExpired,
        subprocess.SubprocessError,
    ) as err:
        return (None, str(err))
    else:
        stdout, stderr = process.communicate()

    return (stdout.strip(), stderr.strip())

def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

def extract_names(text):
    doc = nlp(text)
    names = []
    for ent in doc.ents:
        if ent.label_ == "PERSON" and len(ent.text.split()) >= 2:  # S'assurer que le nom contient au moins un prénom et un nom de famille
            names.append(ent.text)
    return names

def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in skills_set:
            found_skills.add(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in skills_set:
            found_skills.add(ngram)

    return found_skills

if __name__ == '__main__':
    # Chemin du dossier contenant les CV PDF
    pdf_folder_path = r'C:\Users\lando\Desktop\analyse pi\cv'

    # Liste pour stocker les données extraites de tous les CV
    all_data = []

    # Parcourir tous les fichiers PDF dans le dossier
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder_path, filename)
            # Extraction du texte du fichier PDF
            pdf_text = extract_text_from_pdf(pdf_path)
            # Extraction des numéros de téléphone
            phone_number = extract_phone_number(pdf_text)
            # Extraction des adresses e-mail
            emails = extract_emails(pdf_text)
            # Extraction des noms complets
            names = extract_names(pdf_text)
            # Extraction des compétences
            skills = extract_skills(pdf_text)
            # Stockage des données dans la liste
            all_data.append({'Name': names, 'Phone': phone_number, 'Email': emails, 'Skills': skills})

    # Conversion de la liste en DataFrame pandas
    data = pd.DataFrame(all_data)

    # Chemin du fichier CSV
    csv_file_path = r'C:\Users\lando\Desktop\analyse pi\cv\cv_data.csv'

    # Vérifier si le fichier CSV existe
    if os.path.exists(csv_file_path):
        # Charger les données existantes depuis le fichier CSV
        existing_data = pd.read_csv(csv_file_path)
        # Fusionner les données existantes avec les nouvelles données
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        # Supprimer les doublons basés sur l'adresse e-mail
        updated_data.drop_duplicates(subset='Email', inplace=True)
        # Écrire les données mises à jour dans le fichier CSV
        updated_data.to_csv(csv_file_path, index=False)
    else:
        # Écrire les nouvelles données dans le fichier CSV
        data.to_csv(csv_file_path, index=False)
