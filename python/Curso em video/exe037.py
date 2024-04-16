"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversao
1 binario 2 octal 3 hexadecimal"""

n1 = int(input("Digite um número: "))
print("""Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para hexadecimal""")
opcao = int(input("Digite a opção de conversão: "))

if opcao == 1:
    print("O número {}, convertido para binário é: {}".format(n1, bin(n1)[2:]))
elif opcao == 2:
    print("O número {}, convertido para octal é: {}".format(n1, oct(n1)[2:]))
elif opcao == 3:
    print("O número {}, convertido para hexadecimal é: {}".format(n1, hex(n1)[2:]))
else:
    print("Opção inválida.")
