'''Crie um programa que leia um numero inteiro e mostre na tela se ele e par ou impar'''

n1 = int(input("Digite um número: "))
if n1%2==0:
    print("O número {} é par.".format(n1))
else:
    print("O número {} é impar.".format(n1))
