#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
valor_brl = float(input("Qual seu saldo disponível? R$"))
valor_dlr = float(5.01)
cambio = valor_brl / valor_dlr

print("Com este saldo R${:.2f}, você pode comprar ${:.2f} dolares ".format(valor_brl, cambio))
