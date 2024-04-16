"""Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
Equilatero:todos os lados iguais, isoceles:dois lados iguais, escaleno:todos os lados diferentes."""
cores = {"verde" : "\033[32m", "azul" : "\033[34m", "vermelho" : "\033[31m", "limpa" : "\033[m"}
reta1 = float(input("Digite o comprimento da primeira reta em cm: "))
reta2 = float(input("Digite o comprimento da segunda reta em cm: "))
reta3 = float(input("Digite o comprimento da terceira reta em cm: "))
triangulo = ""
tipo = ""

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
    triangulo = "{}Pode formar um triangulo{}".format(cores["verde"], cores["limpa"])
    if reta1 == reta2 and reta2 == reta3:
        tipo = "Triangulo equilatero"
    elif reta1 != reta2 == reta3 or reta2 != reta3 == reta1 or reta3 != reta1 == reta2:
        tipo = "Triangulo isóceles"
    else:
        tipo = "Triangulo escaleno"
else:
    triangulo = "{}Não pode formar um triangulo{}".format(cores["vermelho"], cores["limpa"])
print(triangulo)
print(tipo)