'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
Para salários superiores a 1250 calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%'''
cores = {"verde" : "\033[32m", "azul" : "\033[34m", "vermelho" : "\033[31m", "limpa" : "\033[m"}

salario_atual = float(input("Qual o seu salário: "))
if salario_atual>1250.00:
    salario_novo = salario_atual * 1.1
else:
    salario_novo = salario_atual * 1.15
print("{}Seu salário atualizado é:{} {}R${:.2f}{}".format(cores["azul"], cores["limpa"], cores["verde"],salario_novo, cores["limpa"]))
