#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input("Digite um número inteiro: "))
suc = numero + 1
ant = numero - 1

print("O número escolhido é {}, seu antecessor é {}, e seu sucessor é {}".format(numero, ant, suc))#Poderia calcular dentro do .format (numero, (numero - 1), (numero + 1))


