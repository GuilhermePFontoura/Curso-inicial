'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se ela podem ou nao formar um triangulo'''
cores = {"verde" : "\033[32m", "azul" : "\033[34m", "vermelho" : "\033[31m", "limpa" : "\033[m"}


reta1 = float(input("Digite o comprimento da primeira reta em cm: "))
reta2 = float(input("Digite o comprimento da segunda reta em cm: "))
reta3 = float(input("Digite o comprimento da terceira reta em cm: "))
triangulo = ""
if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
    triangulo = "{}Pode formar um triangulo{}".format(cores["verde"], cores["limpa"])
else:
    triangulo = "{}Não pode formar um triangulo{}".format(cores["vermelho"], cores["limpa"])
print(triangulo)