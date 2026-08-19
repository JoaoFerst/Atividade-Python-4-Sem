numero = int(input("Digite um número inteiro: "))

esta_no_intervalo = numero >= 10 and numero <= 50
eh_par = numero % 2 == 0
atende_as_duas_regras = esta_no_intervalo and eh_par

print(f"Está no intervalo: {esta_no_intervalo}")
print(f"É par: {eh_par}")
print(f"Atende às duas regras: {atende_as_duas_regras}")
