import sys

# Check if an argument is given
if len(sys.argv) != 2:
    print("Tu ne me la mettras pas à l'envers.")
    sys.exit()

arg = sys.argv[1]

# Check if the argument is an even number
if arg.isdigit():
    number = int(arg)
    # Check if the number is even or odd
    if number % 2 == 0:
        print("pair")
    else:
        print("impair")
else:
    # If the argument is an even number, print the error message
    print("Tu ne me la mettras pas à l'envers.")
