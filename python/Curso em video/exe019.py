#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

alunos = [a1, a2, a3, a4]
sorteio = random.choice(alunos)

print("O escolhido entre {} para apagar o quadro é {}!".format(alunos, sorteio))