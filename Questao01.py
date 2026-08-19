nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
    classificacao = "Reprovado"
elif media < 6:
    classificacao = "Recuperação"
elif media < 9:
    classificacao = "Aprovado"
else:
    classificacao = "Aprovado com destaque"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")
