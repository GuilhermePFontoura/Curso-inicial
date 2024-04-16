"""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""
from datetime import date

ano = int(input("Qual o seu ano de nascimento? "))
idade = date.today().year - ano 

if idade < 18:
    print("Você deve se alistar em {} anos.".format(18 - idade))
elif idade > 18:
    print("Voce deveria ter se alistado a {} anos".format(idade - 18))
else:
    print("Você deve se alistar imediatamente!!!")