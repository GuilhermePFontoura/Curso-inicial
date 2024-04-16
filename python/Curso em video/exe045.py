"""Crie um programa que faça o computador jogar jokenpo com você."""

from random import choice 
from time import sleep

jogador = input("Oi vamos jogar jokempo?\nFaça sua escolha!!! ").lower().strip()
maquina = choice(["pedra", "papel", "tesoura"])
resultado = ""
if jogador == maquina:
    resultado = "Empate"
else:
    if jogador == "pedra" and  maquina == "papel":
        resultado = "Ganhei!!!"
    elif jogador == "tesoura" and maquina == "pedra":
        resultado = "Ganhei!!!"
    elif jogador == "papel" and maquina == "tesoura":
        resultado = "Ganhei!!!"
    else:
        resultado = "Você ganhou =( "
print("Minha escolha é...")
sleep(3)
print(maquina.title())
print(resultado)

