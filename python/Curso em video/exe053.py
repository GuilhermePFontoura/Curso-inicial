"""Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços"""
print("Este programa verifica se a frase é um palindromo.")
palavra = input("Qual a frase que deseja consultar: ").strip()
palavra1 = palavra.replace(" ", "").lower()
inverso = ""

for letra in range(len(palavra1) -1, -1, -1):
    inverso = inverso + palavra1[letra]
    if palavra1 == inverso:
        resultado = "É Palindromo!"
    else:
        resultado = "Não é Palindromo!"
print(resultado)