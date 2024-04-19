"""Crie um programa que leia varios numeros inteiros pelo telcado. no final da execução mostre a media entre todos os valores e qual foi o maior e o menor dos valores lidos
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores"""

continuar = 1
num = 0
media = 0
soma = 0
maior = 0
menor = 99999999
cont = 0

while not continuar == 2:
    if continuar == 1:
        num = int(input("Qual número deseja armazenar? "))
        cont = cont + 1
        soma = soma + num
        media = soma / cont
    continuar = int(input("Deseja armazenar mais um número?\n[1]Sim | [2]Não: "))
    if continuar > 2 or continuar == 0:
        print("Opção inválida!")
    if maior < num:
        maior = num
    if num < menor:
        menor = num
    if continuar == 2:
        print("A média dos valores informados é: {}\nO maior é: {}\nO menor é: {}".format(media, maior, menor))
        
    
    
    