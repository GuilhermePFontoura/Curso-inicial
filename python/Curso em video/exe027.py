"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
Ex:Ana Maria de Souza
primeiro: Ana
ultimo:Souza"""
nome = input("Digite seu nome completo: ").strip()
n = nome.title().split()   
primeiro = n[0]
ultimo = n[-1]
print(nome.title())
print(primeiro)
print(ultimo)

