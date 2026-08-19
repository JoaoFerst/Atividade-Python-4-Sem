def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        else:
            return None
    else:
        return None


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, * ou /): ")

resultado = calcular(a, b, operacao)

if resultado == None:
    print("Operação inválida")
else:
    print(resultado)
