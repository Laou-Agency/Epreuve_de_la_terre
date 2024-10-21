import sys

def get_arguments():
    # Retourne la liste des arguments passés au script
    return sys.argv[1:]

def check_argument_count(arguments):
    # Vérifie si le nombre d'arguments est correct
    if len(arguments) != 1:
        print("Tu ne me la mettras pas à l'envers.")
        return False
    return True

def is_valid_number(arg):
    # Vérifie si l'argument est un entier positif
    return arg.isdigit()

def check_even_or_odd(number):
    # Affiche si le nombre est pair ou impair
    if number % 2 == 0:
        print("pair")
    else:
        print("impair")

def main():
    arguments = get_arguments()
    
    if not check_argument_count(arguments):
        return
    
    arg = arguments[0]
    
    while True:
        if is_valid_number(arg):
            number = int(arg)
            check_even_or_odd(number)
            break
        else:
            print("Tu ne me la mettras pas à l'envers.")
            break

if __name__ == "__main__":
    main()