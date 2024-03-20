#5 Faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada
n1 = int(input("Escolha o número para exibir a tabuada: "))
tab = ("1 x {0} = {0}\n2 x {0} = {1}\n3 x {0} = {2}\n4 x {0} = {3}\n5 x {0} = {4}\n6 x {0} = {5}\n7 x {0} = {6}\n8 x {0} = {7}\n9 x {0} = {8}\n10 x {0} = {9} ".format(n1, n1 * 2, n1 * 3, n1 * 4, n1 * 5, n1 * 6, n1 * 7, n1 * 8, n1 * 9, n1 * 10 ))
print("-" * 12)
print(tab)
print("-" * 12)
