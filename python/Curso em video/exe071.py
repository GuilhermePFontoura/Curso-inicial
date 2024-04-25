#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual será o valor a ser sacado(numero inteiro) 
# e o programa vai informar quantas cedulas de cada valor serão entregues, considere que o caixa possui cedulas de 50, 20, 10 e 1


cinquenta = 0
vinte = 0 
dez = 0
um = 0
print("Caixa eletrônico")
valor = int(input("Qual valor deseja sacar? R$"))
while True:
    cinquenta = valor // 50 
    resto = valor % 50
    if resto >= 20:
        vinte = resto // 20
        resto = resto % 20
    if resto >= 10:
        dez = resto // 10
        resto = resto % 10
    if resto >= 1:
        um = resto // 1
        resto = resto % 1
        break
print(f"O valor {valor}, será divido em:\n{cinquenta} notas de cinquenta.\n{vinte} notas de vinte.\n{dez} notas de dez.\n{um} notas de um.")