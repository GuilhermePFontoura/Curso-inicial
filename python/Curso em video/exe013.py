#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
salario = float(input("Salário atual: "))
salario_novo = salario * 1.15

print("Seu novo salário é: R${:.2f}".format(salario_novo))
