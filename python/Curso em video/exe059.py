"""Crie um programa que leia dois valores e mostre um menu na tela
1 somar 2 multiplicar 3 maior 4 novos numeros 5 sair do programa
Seu programa devera realizar a operação solicitada em cada caso"""
from time import sleep

n1 = float(input("Digite o 1º número: "))
sleep(1)
n2 = float(input("Digite o 2º número: "))
opção = 0
maior = n1
while not opção == 5:
    print("""[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR ENTRE ELES
[ 4 ] ALTERAR NÚMEROS
[ 5 ] SAIR""")
    opção = int(input("SELECIONE A OPÇÃO DESEJADA: "))
    print("--"*25)
    if opção == 1:
        print("{} + {} = {}".format(n1, n2, n1 + n2))
        print("--"*25)
        sleep(1)
    if opção == 2:
        print("{} X {} = {}".format(n1, n2, n1 * n2))
        print("--"*25)
        sleep(1)
    if opção == 3:
        if n2 > n1:
            print("O maior número é {}".format(n2))
        else:
            print("O maior número é {}".format(n1))
        print("--"*25)
        sleep(1)
    if opção == 4:
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input("Digite o 2º número: "))
        print("--"*25)
        sleep(1)
    if opção == 5:
        print("\033[32m APLICATIVO FINALIZADO, ESPERO TER AJUDADO!! \033[m")
        print("--"*25)
    if opção == 0 or opção > 5:
        print("\033[31m OPÇÃO INVÁLIDA \033[m")   
        print("--"*25)    
