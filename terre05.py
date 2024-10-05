def find(n, m):
    if m == 0 or n < m:
        print("erreur")
    else:
        q = n // m
        print("résultat:", q)
        r = n % m
        print("reste:", r)

# drive code
find(5, 2)
find(10, 0)
find(3, 5)