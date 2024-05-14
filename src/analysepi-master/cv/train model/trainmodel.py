import spacy
import pandas as pd
from spacy.training import Example
import random

# Charger un modèle pré-entraîné en anglais
nlp = spacy.blank("en")

# Ajouter un composant NER (Named Entity Recognition) au pipeline spaCy
ner = nlp.add_pipe("ner")

# Ajouter des étiquettes pour les entités que nous voulons reconnaître
ner.add_label("Name")
ner.add_label("Email")
ner.add_label("Skills")

# Charger les données des CV à partir d'un fichier CSV
cv_data = pd.read_csv(r"C:\Users\lando\Desktop\analyse pi\cv\train model\UpdatedResumeDataSet.csv")

# Convertir les données en exemples spaCy
examples = []
for _, row in cv_data.iterrows():
    text = row["Resume"]
    entities = []
    for column in cv_data.columns:
        if pd.notnull(row[column]):
            start_idx = text.find(row[column])
            end_idx = start_idx + len(row[column])
            entities.append((start_idx, end_idx, column))
    print("Text:", text)
    print("Entities:", entities)
    examples.append(Example.from_dict(nlp.make_doc(text), {"entities": entities}))

# Entraîner le modèle
n_iter = 100
optimizer = nlp.begin_training()
for i in range(n_iter):
    random.shuffle(examples)
    losses = {}
    for batch in spacy.util.minibatch(examples, size=4):
        nlp.update(batch, drop=0.5, losses=losses, sgd=optimizer)
    print("Iteration", i, "Losses", losses)

# Sauvegarder le modèle entraîné
nlp.to_disk("cv_ner_model")
