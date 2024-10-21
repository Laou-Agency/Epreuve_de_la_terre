import sys

def get_arguments():
    # Return the list of arguments passed to the script
    return sys.argv[1:]

def check_divisor(dvr):
    # Check if divider equals 0
    if dvr == 0:
        print("erreur.")
        return False
    return True

def check_dividend(x, y):
    # Check if dividend is lower than divisor
    if x < y:
        print("erreur.")
        return False
    return True

def division(dvd, dvr):
    quotient = dvd // dvr
    reste = dvd % dvr
    return quotient, reste

def main():
    args = get_arguments()

    # Aguments supposed to be even numbers
    dividend = int(args[0])
    divisor = int(args[1])

    if not check_divisor(divisor):
        return

    if not check_dividend(dividend, divisor):
        return

    quotient, reste = division(dividend, divisor)
    print(f"résultat: {quotient}")
    print(f"reste: {reste}")

if __name__ == "__main__":
    main()