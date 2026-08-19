def eh_palindromo(numero):
    original = numero
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10

    return invertido == original


numero = int(input("Digite um número inteiro positivo: "))

resultado = eh_palindromo(numero)

if resultado:
    print("Palíndromo")
else:
    print("Não palíndromo")
