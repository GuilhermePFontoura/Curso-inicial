#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
valor_produto = float(input("Qual o valor do produto? "))
valor_promoção = valor_produto * 0.95 #poderia ser valor_produto - (valor_produto * 5 / 100)

print("O valor com desconto é R${:.2f}".format(valor_promoção))