import sys

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument.")
    sys.exit(1)

# Vérification que l'argument est un entier positif
arg = sys.argv[1]

# Fonction pour vérifier si une chaîne représente un entier
def est_entier(s):
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()

if not est_entier(arg):
    print("Erreur : L'argument doit être un nombre entier.")
    sys.exit(1)

# Conversion de l'argument en entier
n = int(arg)

# Vérification que le nombre est supérieur ou égal à 2
if n < 2:
    print(f"{n} n'est pas un nombre premier.")
    sys.exit(0)

# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Affichage du résultat
if est_premier(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")