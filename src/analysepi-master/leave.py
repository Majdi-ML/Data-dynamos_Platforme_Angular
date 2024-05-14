import pandas as pd
import numpy as np

# Charger le fichier CSV initial de la table leave
leave_df = pd.read_csv(r'C:\Users\lando\Downloads\Compressed\archive_14\dados.csv')

# Charger le fichier CSV de la table emp_data contenant les codes des employés
emp_data_df = pd.read_excel(r'C:\Users\lando\Desktop\analyse pi\emp_data.xlsx')

# Répéter les lignes existantes pour atteindre 2740 lignes
repeated_leave_df = pd.concat([leave_df] * (2740 // len(leave_df)), ignore_index=True)

# Calculer le nombre de lignes aléatoires à ajouter
remaining_rows = 2740 - len(repeated_leave_df)

# Générer des données aléatoires pour les lignes restantes
random_data = {
    'ID': np.random.randint(1000, 9999, remaining_rows),
    'Reason for absence': np.random.choice(leave_df['Reason for absence'], remaining_rows),
    'Month of absence': np.random.randint(1, 13, remaining_rows),
    'Day of the week': np.random.randint(1, 8, remaining_rows),
    'Seasons': np.random.choice(leave_df['Seasons'], remaining_rows),
    'Transportation expense': np.random.randint(100, 300, remaining_rows),
    'Distance from Residence to Work': np.random.randint(5, 50, remaining_rows),
    'Service time': np.random.randint(1, 25, remaining_rows),
    'Age': np.random.randint(20, 60, remaining_rows),
    'Work load Average/day ': np.random.uniform(200, 400, remaining_rows),
    'Hit target': np.random.randint(80, 100, remaining_rows),
    'Disciplinary failure': np.random.randint(0, 2, remaining_rows),
    'Education': np.random.randint(1, 5, remaining_rows),
    'Son': np.random.randint(0, 5, remaining_rows),
    'Social drinker': np.random.randint(0, 2, remaining_rows),
    'Social smoker': np.random.randint(0, 2, remaining_rows),
    'Pet': np.random.randint(0, 5, remaining_rows),
    'Weight': np.random.uniform(40, 120, remaining_rows),
    'Height': np.random.uniform(140, 200, remaining_rows),
    'Body mass index': np.random.uniform(15, 40, remaining_rows),
    'Absenteeism time in hours': np.random.randint(0, 25, remaining_rows)
}

# Créer un DataFrame à partir des données aléatoires
random_df = pd.DataFrame(random_data)

# Concaténer les lignes répétées et les lignes aléatoires
final_leave_df = pd.concat([repeated_leave_df, random_df], ignore_index=True)

# Sélectionner les codes des employés de la table emp_data pour ajouter à la table leave
emp_codes = emp_data_df['CODE'].tolist()
remaining_emp_codes = emp_codes[len(final_leave_df):]
codes_to_add = emp_codes[:remaining_rows]

# Ajouter les codes des employés à la table leave
final_leave_df['CODE'] = codes_to_add

# Exporter le DataFrame final dans un nouveau fichier CSV
final_leave_df.to_csv(r'C:\Users\lando\Desktop\analyse pi\leave.csv', index=False)
