"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome"""

nome = input("Qual seu nome completo? ").strip()
print("O {}, é um Silva? {}".format(nome, "Silva" in nome.title()))