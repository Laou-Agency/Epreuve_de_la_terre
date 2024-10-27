import sys

def power(base, exponent):
    # Cas limite : tout nombre élevé à la puissance 0 est 1
    if exponent == 0:
        return 1

    # Cas de base : si l'exposant est pair
    if exponent % 2 == 0:
        half_power = power(base * base, exponent // 2)
        return half_power

    # Si l'exposant est impair
    return base * power(base * base, (exponent - 1) // 2)

def is_integer(s):
    if s == '':
        return False
    if s[0] == '-':
        return s[1:].isdigit()
    return s.isdigit()

def main():
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        print("erreur.")
        sys.exit()

    base_str = arguments[0]
    exponent_str = arguments[1]

    # Vérification que la base est un entier
    if not is_integer(base_str):
        print("erreur.")
        sys.exit()
    base = int(base_str)

    # Vérification que l'exposant est un entier non négatif
    if not exponent_str.isdigit():
        print("erreur.")
        sys.exit()
    exponent = int(exponent_str)
    if exponent < 0:
        print("erreur.")
        sys.exit()

    result = power(base, exponent)
    print(result)

if __name__ == "__main__":
    main()
