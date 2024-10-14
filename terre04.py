import sys

def get_argument():
    if len(sys.argv) != 2:
        print("Tu ne me la mettras pas à l'envers.")
        return None
    return sys.argv[1]

def is_valid_number(arg):
    # To check if the argument is an even number
    if arg.isdigit():
        return True
    else:
        return False

def check_even_or_odd(number):
    if number % 2 == 0:
        print("pair")
    else:
        print("impair")

def main():
    arg = get_argument()
    if arg is None:
        return

    # Using a while loop for managing errors
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