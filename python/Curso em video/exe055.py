"""Faça um programa que leia o peso de cinco pessoas no final mostre qual foi o maior e o menor peso lidos"""
"""peso = []
for c in range (1,6):
    n1 = float(input("Qual o peso da {}º pessoa: ".format(c)))
    peso.append(n1)

peso.sort()
maior = peso[-1]
menor = peso[0]

print("O menor peso é {}kg, e o maior é {}kg.".format(menor, maior))"""

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Quantos quilos tem a {}º pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior, menor)
