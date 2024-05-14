import os
import glob
import pandas as pd

# Chemin vers le répertoire contenant les fichiers CSV
directory = r"C:\Users\lando\Desktop\analyse pi\data"

# Modèle de nom de fichier à rechercher
file_pattern = "phantombuster-all-leads-02132024*.csv"

# Liste des chemins des fichiers correspondant au modèle de nom de fichier
files = glob.glob(os.path.join(directory, file_pattern))

# Initialiser une liste pour stocker les DataFrames de chaque fichier CSV
dfs = []

# Lire chaque fichier CSV et ajouter son DataFrame à la liste
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

# Fusionner tous les DataFrames en un seul DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Enregistrer le DataFrame fusionné dans un fichier CSV
merged_df.to_csv("merged_leads.csv", index=False)

print("Tous les fichiers ont été fusionnés avec succès dans 'merged_leads.csv'.")
