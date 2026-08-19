n = int(input("Digite um número: "))

fatorial = 1

for numero in range(1, n + 1):
    fatorial = fatorial * numero

print(f"Fatorial de {n}: {fatorial}")
