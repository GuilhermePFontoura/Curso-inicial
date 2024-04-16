""""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou entao o emprestimo será negado"""
valor_casa = float(input("Qual o valor total da casa? "))
salario = float(input("Qual o seu salário bruto? "))
financiamento = float(input("Em quantos anos deseja financiar? "))
prestacao = valor_casa / (financiamento * 12 ) #Pegar o valor da mensalidade
aceite = salario * 0.3 #Pegar 30% do salario para calculos
if prestacao <= aceite:
    print("Financiamento aprovado! O valor da prestação é: R${:.2f}".format(prestacao))
else:
    print("Financiamento não aprovado!")


