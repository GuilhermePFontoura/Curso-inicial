# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando o flag
n = 0
cont = 0
soma = 0

while True:
    n = int(input("Qual número deseja armazenar para soma: "))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f"Você passou {cont} números e a soma entre eles é: {soma}")