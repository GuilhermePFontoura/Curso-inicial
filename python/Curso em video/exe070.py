#Crie um programa que leia o nome e o preco de varios produtos. O programa deverá perguntar se o usuario vai continuar. No final mostre:
#Qual é o total gasto na compra. Quantos produtos custam mais de 1000. Qual é o nome do produto mais barato.

nome_produto = input("Produto: ")
preco_produto = float(input("Preço: R$"))
cont = 0 
total = 0
maisDeMil = 0
nomeMaisBarato = nome_produto
valorMaisBarato = preco_produto
while True:
    total += preco_produto
    if preco_produto >= 1000:
        maisDeMil +=1
    if valorMaisBarato > preco_produto:
        valorMaisBarato = preco_produto
        nomeMaisBarato = nome_produto
    continuar = input("Deseja inserir mais produtos?").strip().upper()[0]
    if continuar == "S":
        nome_produto = input("Produto: ")
        preco_produto = float(input("Preço: R$"))
    if continuar == "N":
        break

print(f"Dos produtos cadastrados:\n{total} é o total.\n{maisDeMil} custam mais de R$1000.\n{nomeMaisBarato} é o produto mais barato.")