"""c = 1
while c < 10:
    print(c)
    c = c + 1
print("fim!!")"""

"""r = 0
while r < 21:
    cartas = int(input("Digite um valor pra tentar chegar em 21: "))
    r = r + cartas
    if r == 21:
        print("Você chegou a 21 parabéns!!!")
    elif r > 21:
        print("Você perdeu, já passou de 21!")"""
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input("Digite um valor: "))
    if n % 2 == 0 and n != 0:
        par = par + 1
    else:
        impar = impar + 1
print("Você digitou {} números pares e {} números impares.".format(par, impar))
