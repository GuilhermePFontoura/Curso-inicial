"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
- A media de idade do grupo.
- Qual e o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos"""
media = 0
grupo = 4
homem_mais_velho = 0
somaidade = 0
nomevelho = ""
mulheres_menores = 0

for i in range (1, grupo + 1):
    nome = input("Qual o nome da {}º pessoa: ".format(i)).strip().title()
    idade = int(input("Qual a idade da {}º pessoa: ".format(i)))
    sexo = input("Qual o sexo da {}º pessoa: [M] ou [F]: ".format(i)).strip().upper()
    somaidade = somaidade + idade #soma todas as idades do grupo
    if i == 1 and sexo == "M":
        homem_mais_velho = idade
        nomevelho = nome
    if sexo == "M" and idade > homem_mais_velho:
        homem_mais_velho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulheres_menores = mulheres_menores + 1    

media = somaidade / grupo # calcula a media das idades do grupo

print("A média de idade do grupo é {} anos!".format(media))
print("O homem mais velho tem {}, e é o {}".format(homem_mais_velho, nomevelho))
print("Existem {} mulheres menores de 20 anos no grupo!".format(mulheres_menores))


