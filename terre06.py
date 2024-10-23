import sys

def inverser_chaine(chaine):
    return chaine[::-1]

def main():
    arguments = sys.argv[1:]
    
    if not arguments:
        print("Erreur : Aucun argument fourni. Veuillez fournir au moins une chaîne à inverser.")
        return arguments

    resultats = []
    for arg in arguments:
        # Inverser chaque chaîne, y compris celles avec des symboles
        resultats.append(inverser_chaine(arg))
    
    # Afficher tous les résultats sur une seule ligne
    print(" ".join(resultats))
    
    return arguments

if __name__ == "__main__":
    main()