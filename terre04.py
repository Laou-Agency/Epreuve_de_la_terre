try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Tu ne me la mettras pas à l'envers.")
    exit()

if num % 2 == 0:
    print("pair")
else:
    print("impair")

if num < 0:
    print("Tu ne me la mettras pas à l'envers.")