import re 
file_path = r'C:\Users\User\OneDrive\Bureau\Problem Solving question 1\document.txt'

with open(file_path, 'r') as file:
    content = file.read()

# Fonction pour extraire la valeur d'étalonnage
def extract_etalonnage_value(line):
    digits = re.findall(r'\d', line)
    
    if len(digits) == 1:
        
        return digits[0] + digits[0]
    elif len(digits) > 1:
        
        return digits[0] + digits[-1]

with open(file_path, 'r') as file:
    lines = file.readlines()

etalonnage_values = [extract_etalonnage_value(line.strip()) for line in lines if extract_etalonnage_value(line.strip()) is not None]

print(etalonnage_values)

# Calculer la somme des valeurs d'étalonnage
sum_etalonnage_values = sum(int(value) for value in etalonnage_values)

print("Somme des valeurs d'étalonnage :", sum_etalonnage_values)