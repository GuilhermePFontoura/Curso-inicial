#Escreva um programa que leia um valor em metros e exiba convertido em centimetro e milimetros
m = float(input("Quantos metros tem de altura a parede? "))
cent = m * 100
mili = m * 1000

print("A parede tem {}m que corresponde a {}cm e {}mm ".format(m, cent, mili))