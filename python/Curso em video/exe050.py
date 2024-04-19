"""Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere."""
s = 0 

for c in range (0, 6):
    v = int(input("Digite o valor que deseja somar: "))
    if v % 2 == 0:
        s = s + v
print(s)