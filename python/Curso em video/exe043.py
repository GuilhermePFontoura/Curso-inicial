"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal, entre 25 e 30: sobrepeso, 30 até 40:obesidade, acima de 40: obesidade morbida"""
print("Vamos calcular seu IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
calculo_imc = peso / altura ** 2
resultado = ""

if calculo_imc < 18.5:
    resultado = "abaixo do peso"
elif calculo_imc <= 25:
    resultado = "no peso ideal"
elif calculo_imc <= 30:
    resultado = "com sobrepeso"
elif calculo_imc <= 40:
    resultado = "com obesidade"
else :
    resultado = "com obesidade morbida"
print("Seu imc é {:.1f} e você está {}.".format(calculo_imc, resultado))
