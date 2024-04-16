"""Crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final, de acordo com a media atingida:
Media abaixo de 5: reprovado, media entre 5 e 6.9: recuperação, media 7 ou superior: aprovado!"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua nota final é: {:.1f}".format(media))
if media < 5:
    print("Aluno reprovado!")
elif media < 7:
    print("Aluno em recuperação!")
else:
    print("Aluno aprovado! Parabéns")