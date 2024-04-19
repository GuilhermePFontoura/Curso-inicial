"""Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
ex 0-1-1-2-3-5-8"""

qtd_elementos = int(input("Quantos elementos da sequencia de fibonacci deseja visualizar?"))
c = 0
penult = 0
ult = 1
print(penult, end="-")
print(ult, end="-")
while c != qtd_elementos :
    c = c + 1
    res = penult + ult
    penult = ult
    ult = res
    print(ult, end="-")
    
    
        
    