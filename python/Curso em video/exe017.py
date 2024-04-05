#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
cateto_a = float(input("Digite o comprimento do cateto adjacente: "))
cateto_o = float(input("Digite o comprimento do cateto oposto: "))
hipot = math.hypot(cateto_a, cateto_o)# poderia ser (cateto_o ** 2 + cateto_a ** 2) ** (1/2)


print("O comprimento da hipotenusa é {:.2f}".format(hipot))
