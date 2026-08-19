limite = int(input("Digite o limite: "))
divisor = int(input("Digite o divisor: "))

soma = 0

for numero in range(1, limite + 1):
    if numero % divisor == 0:
        soma = soma + numero

print(f"Soma dos múltiplos: {soma}")
