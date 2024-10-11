import sys

# Vérifier s'il y a bien un argument fourni
if len(sys.argv) > 1:
    start_letter = sys.argv[1]  # Récupérer la lettre donnée en argument
    if len(start_letter) == 1 and 'a' <= start_letter <= 'z':  # Vérifier que c'est bien une lettre minuscule
        for letter in range(ord(start_letter), ord('z') + 1):
            print(chr(letter), end="")
        print()  # Retour à la ligne après l'alphabet
    else:
        print("Veuillez fournir une seule lettre minuscule comme argument.")
else:
    print("Veuillez fournir une lettre comme argument.")
