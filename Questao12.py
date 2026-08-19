def potencia(base, expoente):
    resultado = 1

    for numero in range(expoente):
        resultado = resultado * base

    return resultado


base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)

print(resultado)
