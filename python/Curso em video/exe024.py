"""Crie um programa que leia o nome de uma cidade e diga se ela 
começou ou nao com o nome "Santo" """

cidade = str(input("Qual a sua cidade? ")).strip()
cidade = cidade.split()
primeira_palavra = cidade[0]
print("Santo" in primeira_palavra.title())