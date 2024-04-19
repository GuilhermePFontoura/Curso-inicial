"""Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while"""

termo = int(input("Qual o primeiro número da Progressão? "))
razao = int(input("Qual a razão da Progressão? "))
limite = 10 * razao
resultado = termo

print(termo)
while resultado < limite:
    resultado = resultado + razao
    print(resultado)
