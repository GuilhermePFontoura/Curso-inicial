"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
ate 9 anos mirim, ate 14 anos infantil, ate 19 anos junior, ate 20 anos senior, acima master"""
from datetime import date

ano_nascimento = int(input("Bom dia, atleta, em que ano você nasceu? "))
idade = date.today().year - ano_nascimento

if idade < 10:
    print("Sua categoria é mirim!")
elif idade < 15:
    print("Sua categoria é infantil!")
elif idade < 20:
    print("Sua categoria é Júnior!")
elif idade < 26:
    print("Sua categoria é Senior!")
else:
    print("Sua categoria é Master!")
