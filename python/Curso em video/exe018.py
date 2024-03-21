#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input("Digite o angulo: "))
cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("O angulo {:.2f}º tem o valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.".format(angulo, seno, cosseno, tangente))

