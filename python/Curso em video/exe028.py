'''Faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
O programa devera escrever na tela se o usuário venceu ou perdeu'''
from random import randint
from time import sleep  #sleep para dar uma pausa dramatica 
num_aleatorio =  randint(0, 5)
num_escolha = int(input("Digite um número de 0 a 5: "))
print("Processando...")
sleep(3)
if num_aleatorio == num_escolha:
    print("Você acertou!!!")
else:
    print("Você perdeu!!!")
print("O número aletório é: {}".format(num_aleatorio))
