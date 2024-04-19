"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
from time import sleep

interação = int(input("""Você quer começar a contagem?
[1] SIM
[2] NÃO
Digite a sua opção: """))
for c in range (10, -1, -1):
    if interação == 1:
        print(c)
        sleep(1)
if interação == 1:
    print("BOOOOOOOOOOOMMMMM")
else:
    print("Aguardando autorização para contagem.")