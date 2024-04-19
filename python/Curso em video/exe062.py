"""Melhore o desafio 61, perguntando para o usuáro se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos"""

termo = int(input("Qual o primeiro número da Progressão? "))
razao = int(input("Qual a razão da Progressão? "))
limite = 10 * razao  #calcula o número maximo que vai chegar conforme a razão escolhida
resultado = termo #Recebe o termo para calculo

print(termo)
while resultado <= limite:
    resultado = resultado + razao #calcula o termo escolhido + a razão escolhida até o limite definido
    print(resultado)
    if resultado == termo + 10*razao or resultado == limite:
        novo_resultado = int(input("Quantos termos a mais deseja ver agora? "))
        limite = limite + novo_resultado * razao
        while resultado < limite:
            resultado = resultado + razao
            print(resultado)
        