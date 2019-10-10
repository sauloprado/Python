# encoding: utf-8

# Média
# Soma dos Valores / Número de Valores

nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))

media = (nota1+nota2)/2

print("Sua Média é %f" % media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")