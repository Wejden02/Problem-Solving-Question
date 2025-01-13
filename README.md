Ce Question  consiste à extraire des valeurs d'étalonnage spécifiques depuis un document texte. Chaque ligne du document contient des caractères alphanumériques, et la valeur d'étalonnage est déterminée en combinant le premier et le dernier chiffre de chaque ligne. Si une ligne ne contient qu'un seul chiffre, la valeur d'étalonnage sera ce chiffre répété deux fois.

## Le script Python suivant effectue les opérations suivantes :

1. Lecture du fichier texte: Le fichier contenant les lignes de texte est ouvert et son contenu est récupéré.
2. Extraction des valeurs d'étalonnage: Pour chaque ligne, le script recherche les chiffres. Le premier et le dernier chiffre sont extraits et combinés pour former une valeur à deux chiffres.
3. Calcul de la somme des valeurs d'étalonnage: Une fois toutes les valeurs extraites, elles sont additionnées pour obtenir une somme totale.
