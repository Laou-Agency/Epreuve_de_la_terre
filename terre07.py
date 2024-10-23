import sys
import re

def get_argument():
    arguments = sys.argv[1:]
    count = 0
    for arg in arguments:
        count += 1
        if count > 1:
            break
    if count != 1:
        print("erreur.")
        sys.exit()
    for arg in arguments:
        return arg  # Retourne le seul argument fourni

def count_chars(s):
    count = 0
    for _ in s:
        count += 1
    return count

def is_number(s):
    # Utilise une expression régulière pour vérifier si la chaîne est un nombre
    number_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    s = s.strip()
    if number_pattern.match(s):
        return True
    else:
        return False

def main():
    arg = get_argument()
    if is_number(arg):
        print("erreur.")
        sys.exit()
    else:
        print(count_chars(arg))

if __name__ == "__main__":
    main()