#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
numero = int(input("Digite seu número: "))
dob = numero * 2
trip = numero * 3
raiz_quadrada = numero ** (1/2)

print("O número escolhido é {}, o dobro é {}, o triplo é {} e a raiz quadrada é {}".format(numero, dob, trip, raiz_quadrada)) # raiz quadrada pode ser feito com pow(n, (1/2))

