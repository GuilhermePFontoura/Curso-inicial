"""Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500."""

s = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        s = s + c
print("A soma entre os números impares que são multiplos de tres e que se encontram no intervalo de 1 a 50 é: {}".format(s))
