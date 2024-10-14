import sys

def check_uppercase(input_string):
    return any(char.isupper() for char in input_string)

while True:
    user_input = input("Enter a lowercase letter: ")

    if check_uppercase(user_input) or len(user_input) != 1 or not user_input.isalpha():
        print("Error: Please enter a single lowercase letter.")
    else:
        break  # Sortir de la boucle lorsque l'entrée est valide

# Boucle pour afficher l'alphabet à partir de la lettre donnée
for letter in range(ord(user_input), ord('z') + 1):
    print(chr(letter), end="")  # Utilisation correcte de `chr(letter)`

# Retour à la ligne à la fin
print()