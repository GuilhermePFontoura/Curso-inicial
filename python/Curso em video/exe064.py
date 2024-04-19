"""Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condicao de parada. 
No final mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999 """
c = 0 
s = 0
cont = 0
while c != 999:
    c = int(input("Qual número deseja incluir?(Digite 999 para finalizar): "))
    if c != 999:
        cont = cont + 1
        s = s + c
print("Você digitou {} números e a soma entre eles foi {}.".format(cont, s))
    
        
    