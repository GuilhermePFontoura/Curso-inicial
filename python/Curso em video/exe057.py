"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F" 
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = ""
while sexo != "M":
    sexo = input("Qual o sexo?(M ou F): ").upper().strip()
    if sexo == "M" or sexo == "F":
        print("Sexo cadastrado com sucesso.")
        break
    else:
        print("Sexo não cadastrado corretamente!!!")