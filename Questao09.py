n = int(input("Digite um número maior que 1: "))

quantidade_divisores = 0

for numero in range(1, n + 1):
    if n % numero == 0:
        quantidade_divisores = quantidade_divisores + 1

if quantidade_divisores == 2:
    print("Primo")
else:
    print("Não primo")
