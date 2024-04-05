'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80 mostre uma mensagem dizendo que ele foi multado
A multa vai custar 7 por cada km a cima do limite'''

velocidade = int(input("Digite a velocidade que passou no radar: "))
multa = (velocidade - 80) * 7
if velocidade>80:
    print("Você foi multado!")
if velocidade>80:
    print("O valor da multa é R${:.2f}".format(multa))
else:
    print("Você não foi multado!")
