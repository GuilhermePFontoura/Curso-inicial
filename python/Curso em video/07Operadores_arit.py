#Operadores aritmeticos 
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)
print(pow(4,3))#função para elevar a potencia
print(81**(1/2))#calculo para descobrir a raiz quadrada
print("-" * 30)#multiplicar caracteres ou palavras

#ordem precedência
#1 - ()  2 - ** 3 - * , /, //, %  4 - +, -
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

#Editar informação do print
n = input("Qual seu nome? ")
n1 = float(input("Digite um número com varias casas decimais: "))
print("Prazer em te conhecer {:<20}!".format(n))#alinhar a esquerda
print("Prazer em te conhecer {:>20}!".format(n))#alinhar a direita
print("Prazer em te conhecer {:^20}!".format(n))#centralizar
print("Prazer em te conhecer {:1^20}!".format(n))#centralizar e inserir o caractere (1)
print("O número decimal é {:.3f}".format(n1)) #Definir quantidade de casas decimais



