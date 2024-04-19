"""Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmetica. no final mostre os 10 primeiros termos dessa progressão"""

termo = int(input("Qual o primeiro número da Progressão? "))
razao = int(input("Qual a razão da Progressão?"))
limite = 11 * razao

for c in range (termo, limite, razao):
    print(c)
