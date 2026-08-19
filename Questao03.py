a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b and b == c:
    print("Todos iguais")
else:
    maior = a
    menor = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    if b < menor:
        menor = b

    if c < menor:
        menor = c

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
