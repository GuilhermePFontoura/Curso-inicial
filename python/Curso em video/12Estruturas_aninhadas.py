nome = input("Qual seu nome? ")

if nome == "Guilherme":
    print("Que nome bonito, {}!".format(nome))
elif nome == "João":
    print("Que nome normal, {}!".format(nome))
elif nome in "Ana Joana Maria Claudia":
    print("Você é uma garota, {}!".format(nome))
else:
    print("Seu nome é bem normal, {}!".format(nome))
    