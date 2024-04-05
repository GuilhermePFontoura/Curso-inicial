import math  #importa todo a biblioteca math
import random 
from math import sqrt #importa só sqrt de math

num = int(input("Digite um número: "))
raiz = math.sqrt(num) #sqrt calcula a raiz do valor
print("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))# math.ceil arredonda para cima e floor para baixo
rand = random.randint(1, 10)# pedir um número aleatorio entre 1 e 10 neste caso




