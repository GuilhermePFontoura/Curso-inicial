#Faça um programa que joge par ou impar com o computador. O jogo só será interrompido quando o jogador Perder, mostrando o total de vitorias 
#consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input("Faça sua escolha: "))
    par_ou_impar = int(input("[1]IMPAR ou [2]PAR\nPar ou impar: "))
    resultado = (computador + jogador) % 2
    if par_ou_impar == 1:
        if resultado == 0:
            print(f"Minha escolha foi {computador} e a sua {jogador}. Ganhei!!!")
            break
        elif resultado == 1:
            print(f"Minha escolha foi {computador} e a sua {jogador}. Você venceu!")
            vitorias += 1
    if par_ou_impar == 2:
        if resultado == 0:
            print(f"Minha escolha foi {computador} e a sua {jogador}. Você venceu!")
            vitorias += 1
        elif resultado == 1:
            print(f"Minha escolha foi {computador} e a sua {jogador}. Ganhei!!!")
            break
print(f"O jogo acabou e você ganhou {vitorias} vezes.")
            