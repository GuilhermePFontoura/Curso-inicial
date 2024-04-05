'''Desenvolva um programa que pergunte a distancia de uma viagem em km
Calcule o preço da passagem cobrando 0,50 por km para viagens até 200km
E 0,45 para viagens mais longas'''
distancia = int(input("Digite a distância da viagem: "))
if distancia<=200:
    print("O custo da sua viagem será de R${:.2f}".format(distancia*0.5))
else:
    print("O custo da sua viagem será de R${:.2f}".format(distancia*0.45))