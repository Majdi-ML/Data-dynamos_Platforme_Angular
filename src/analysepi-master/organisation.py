import csv

# Fonction pour lire les données à partir du fichier CSV
def lire_donnees_csv(nom_fichier):
    donnees = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            donnees.append(row)
    return donnees

# Fonction pour écrire les données dans un fichier CSV
def ecrire_donnees_csv(nom_fichier, donnees):
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['linkedinProfileUrl', 'fullName', 'firstName', 'lastName', 'linkedinHeadline', 'location', 'linkedinProfileSlug', 'id', 'createdAt', 'updatedAt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Écriture de l'en-tête
        writer.writeheader()
        
        # Écriture des lignes de données
        for row in donnees:
            writer.writerow(row)

# Fonction pour nettoyer les données
def nettoyer_donnees(donnees):
    donnees_propres = []
    for ligne in donnees:
        # Vérifie si la ligne contient des virgules ou les phrases spécifiées, ou si elle est vide
        if not any(keyword in ligne.values() for keyword in [",", "Export limit reached - Get more with our premium plans", "Upgrade to export all your data with the link below:"]) and any(value.strip() for value in ligne.values()):
            donnees_propres.append(ligne)
    return donnees_propres

# Chemin du fichier CSV à nettoyer et modifier
fichier_a_modifier = 'C:/Users/lando/Desktop/analyse pi/donnees_employes_organisees.csv'

# Lire les données du fichier CSV
donnees = lire_donnees_csv(fichier_a_modifier)

# Nettoyer les données
donnees_nettoyees = nettoyer_donnees(donnees)

# Réécrire les données modifiées dans le même fichier CSV
ecrire_donnees_csv(fichier_a_modifier, donnees_nettoyees)

print("Les données ont été nettoyées avec succès dans le fichier", fichier_a_modifier)
