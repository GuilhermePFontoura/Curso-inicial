soma = 0
cont = 0
num = 0
while True:
    num = int(input("Qual valor deseja adicionar a soma: "))
    cont += 1
    if num == 999:
        break
    soma += num
print(f"Você digitou {cont} números e a soma deles é {soma}")