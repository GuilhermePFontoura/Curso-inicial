"""Crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja são maiores."""
from datetime import date

"""datas_de_nasc = []

for c in range(0, 7):
    data = int(input("Qual a data de nascimento: "))
    datas_de_nasc.append(data)

maiores = 0
menores = 0

for data in datas_de_nasc:
    data1 = date.today().year - data
    if data1 >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print("Da lista informada {}, são maiores de idade e {}, são menores de idade.".format(maiores, menores))"""

atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    data = int(input("Em que ano a {}º pessoa nasceu? ".format(c)))
    idade = atual - data
    if idade >= 18:
        maior = maior + 1
    elif idade < 18:
        menor = menor + 1
print("Da lista informada {}, são maiores de idade e {}, são menores de idade.".format(maior, menor))


