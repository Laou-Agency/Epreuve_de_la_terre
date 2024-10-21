import sys

def get_arguments():
    # Stocker les arguments dans une variable avant de les retourner
    arguments = sys.argv[1:]
    return arguments

def check_divisor(divisor):
    # Vérifier si le diviseur est égal à 0
    if divisor == 0:
        print("erreur.")
        return False
    return True

def check_dividend(dividend, divisor):
    # Vérifier si le dividende est inférieur au diviseur
    if dividend < divisor:
        print("erreur.")
        return False
    return True

def is_integer(value):
    # Vérifier si une valeur peut être convertie en entier
    is_valid = value.lstrip('-').isdigit()
    if not is_valid:
        print(f"erreur: '{value}' n'est pas un entier valide.")
    return is_valid

def division(dividend, divisor):
    # Calculer le quotient et le reste de la division
    quotient = dividend // divisor
    reste = dividend % divisor
    return quotient, reste

# Exécution directe du programme avec gestion d'erreurs
arguments = get_arguments()

# Vérification que deux arguments sont fournis
nombre_arguments = len(arguments)
if nombre_arguments != 2:
    print("erreur: deux arguments sont nécessaires.")
else:
    # Récupération des valeurs des arguments
    argument_1 = arguments[0]
    argument_2 = arguments[1]

    # Vérification si les arguments sont des entiers
    if is_integer(argument_1) and is_integer(argument_2):
        dividend = int(argument_1)
        divisor = int(argument_2)

        # Vérification des conditions de division
        est_diviseur_valide = check_divisor(divisor)
        est_dividende_valide = check_dividend(dividend, divisor)

        if est_diviseur_valide and est_dividende_valide:
            quotient, reste = division(dividend, divisor)
            print(f"résultat: {quotient}")
            print(f"reste: {reste}")
