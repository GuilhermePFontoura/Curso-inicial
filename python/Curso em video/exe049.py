"""Refaça o desafio 009 mostrando a tabuada de um numero que o usuario escolher só que agora utilizando um laço for"""

num1 = int(input("""Selecione a tabuada desejada
[1]
[2]
[3]
[4]
[5]
[6]
[7]
[8]
[9]
"""))

for c in range (1, 11):
    print("{} X {} = {}".format(c, num1, c*num1))