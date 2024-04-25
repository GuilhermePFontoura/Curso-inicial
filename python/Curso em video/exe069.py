#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou nao continuar. No final mostre:
#Quantas pessoas tem mais de 18 anos.  Quantos homens foram cadastrados.  Quantas mulheres com menos de 20 anos.
cont = 0
idade18 = 0
homens = 0
mulheres20 = 0
continuar = "S"
sexo = "MF"
while True:
    if sexo in "MF":
        if continuar == "N":
            break
        elif continuar == "S":
            cont += 1
            idade = int(input(f"Qual a idade da {cont}º pessoa: "))
            sexo = input(f"Qual o sexo da {cont}º pessoa:(M ou F):").strip().upper()[0]
            continuar = input("Você deseja inserir mais informações? ").strip().upper()[0]
            if idade >= 18:
                idade18 += 1
            if sexo == "M":
                homens += 1
            if idade < 20 and sexo == "F":
                mulheres20 += 1
        else:
            continuar = input("Você deseja inserir mais informações? ").strip().upper()[0]
    elif sexo not in "MF":
        sexo = input(f"Opção invalida: Qual o sexo da {cont}º pessoa:(M ou F):").strip().upper()[0] 
        if sexo == "M":
            homens += 1
        if idade < 20 and sexo == "F":
            mulheres20 += 1
            
    
print(f"Da lista informada:\n{idade18} tem mais de 18 anos.\n{homens} são homens.\n{mulheres20} são mulheres com menos de 20 anos.")
        