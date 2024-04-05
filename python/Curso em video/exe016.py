#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porçao inteira
#ex Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
import math
n = float(input("Digite um número decimal: "))
print("a parte inteira do número {} é {}".format(n, math.trunc(n)))#poderia ser int(n), traria apenas a parte inteira do numero.