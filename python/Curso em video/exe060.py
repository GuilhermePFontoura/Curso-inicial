"""Faça um programa que leia um numero qualquer e mostre o seu fatorial.
ex 5!= 5x4x3x2x1 = 120"""

num = int(input("Qual numero que saber o fatorial: "))
resultado = num 
mult = 0
# for i in range(1, num ):
#     resultado = resultado * i
# print("O fatorial do número {}!, é : {} ".format(num, resultado))

while mult < num - 1:
    mult = mult + 1
    resultado = mult * resultado
print("O fatorial do número {}!, é : {} ".format(num, resultado))
