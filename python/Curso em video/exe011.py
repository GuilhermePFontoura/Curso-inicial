#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
#e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
area = altura * largura 
tinta = area / 2
print("A área da parede é de {}m², você vai precisar de {}l de tinta".format(area, tinta))

