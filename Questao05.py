n = int(input("Digite um número: "))

while n >= 0:
    if n > 0 and n % 5 == 0:
        print(f"{n} é divisível por 5")
    else:
        print(n)

    n = n - 1
