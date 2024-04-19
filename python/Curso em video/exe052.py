"""Desenvolva um programa que leia um número inteiro e diga se ele é ou nao um numero primo"""

n1 = int(input("Digite o número que deseja saber se é primo:"))
s = 0

if n1 >= 1:
    for c in range (1, n1+1):
        if n1 % c == 0:
            s = s + c
            if s > (n1 + 1):
                print("Não é primo!")
            elif s == (n1+1):
                print("É primo!")
