import sys

def binary_search_sqrt(n):
    if n < 0:
        print("erreur.")
        sys.exit()
    
    low = 0.0
    high = max(1.0, n)
    epsilon = 1e-7  # Précision jusqu'à 6 décimales

    while high - low > epsilon:
        mid = (low + high) / 2.0
        square = mid * mid
        if abs(square - n) <= epsilon:
            return round(mid, 6)
        elif square < n:
            low = mid
        else:
            high = mid

    return round((low + high) / 2.0, 6)

def main():
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("erreur.")
        sys.exit()

    arg = arguments[0]
    if not arg.isdigit():
        print("erreur.")
        sys.exit()

    n = int(arg)
    result = binary_search_sqrt(n)
    print(result)

if __name__ == "__main__":
    main()
