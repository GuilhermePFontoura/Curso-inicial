"""Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer."""

from random import randint
from time import sleep
cont = 0
num_jog = 99
num_comp = randint(0, 10)

print("Vou pensar em um número de 0 a 10, vamos ver se você acerta!")
sleep(1)
while num_jog != num_comp:
    num_jog = int(input("Digite um número de 0 a 10: "))
    sleep(1)
    cont = cont + 1
    if num_jog == num_comp:
        print("O número que pensei foi o {}, e você acertou em {} tentativas".format(num_comp, cont))
    if num_jog != num_comp:
        print("Você errou, tente novamente")
    