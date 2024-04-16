"""Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
a vista:10%desconto, a vista cartão:5% de desconto, em até 2x no cartão:preço normal, 3x ou mais :20% de juros"""

preco = float(input("Qual o valor de sua compra? "))
forma_pgt = input("Qual a sua forma de pagamento? ").lower().strip()
preco_final = ""
parcelamento = ""

if forma_pgt == "dinheiro" or forma_pgt == "pix":
    preco_final = preco * 0.90
elif forma_pgt == "cartão" or forma_pgt == "cartao":
    parcelamento = int(input("Quantas vezes quer fazer o pagamento? "))
    if parcelamento == 1:
        preco_final = preco * 0.95
    elif parcelamento == 2:
        preco_final = preco
    else:
        preco_final = preco * 1.2
print("Na forma de pagamento {}, o valor a ser pago é R${:.2f}.".format(forma_pgt, preco_final))
