def classificar_numero(numero):
    if numero == 0:
        return "zero"
    elif numero > 0:
        if numero % 2 == 0:
            return "positivo e par"
        else:
            return "positivo e ímpar"
    else:
        if numero % 2 == 0:
            return "negativo e par"
        else:
            return "negativo e ímpar"


numero = int(input("Digite um número: "))

resultado = classificar_numero(numero)

print(resultado)
