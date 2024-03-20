nome = input("Digite aqui seu nome:")
email = input("Digite aqui seu email:")

posicao = email.find("@")
servidor = email[posicao+1:]

posicao2 = nome.find(" ")
primeiro_nome = nome[:posicao2]

posicao3 = email[1:posicao]
email_trocado = email.replace(posicao3, "***********")



print(servidor) #1 exercicio
print(primeiro_nome) #2 exercicio
print("Usuário", primeiro_nome, "cadastrado com sucesso com o email:"+ email ) #3 exercicio
print("Enviamos um link de confirmação para o email", email_trocado) #4 exercicio