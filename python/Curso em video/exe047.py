"""Faça um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50."""
par_ou_impar = int(input("""A aplicação mostrará números impares ou pares até 50.
[ 1 ] IMPAR
[ 2 ] PAR
Escolha qual opção deseja:  """))

for c in range (par_ou_impar, 51, 2):
    if par_ou_impar == 1 or par_ou_impar == 2:
        print(c)
else:
    print("Opção invalida")