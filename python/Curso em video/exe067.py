# Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuario. o programa sera interrompido quando o numero solicitado for negativo
cont = 0
fator = int(input("Qual número deseja saber a tabuada: "))
while True:
    if fator < 0:
        print("Programa finalizado!")
        break
    else:
        if cont < 10:
            cont += 1
            resultado = fator * cont
            print(f"{fator} x {cont} = {resultado}")
        else:
            fator = int(input("Qual número deseja saber a tabuada: "))
            cont = 0
        
        