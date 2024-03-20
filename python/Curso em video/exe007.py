#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nota1 = float(input("Nota do trabalho 1: "))
nota2 = float(input("Nota do trabalho 2: "))
media = (nota1 + nota2) / 2

print("A nota final é: {:.1f}".format(media))

