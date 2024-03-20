faturamento = 1000
custo = 700

lucro = faturamento - custo

print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
print("Faturamento:" + str(faturamento) + ", Custo:" + str(custo) + ", Lucro:" + str(lucro))

email = "EMAIL_falso@gmail.com"
print(email.lower()) #DEIXAR EM LETRAS MINUSCULAS
print(email.find("@")) #find procura onde está o elemento -1 não existe, se encontrar vai passar o indice
print(email[12])#Traz o caractere que está na posição que solicitou

posicao = email.find("@")
servidor = email[posicao+1:] # : traz tudo que vier após ou antes do valor solicitado    :posicao ou posicao:
print(servidor)

#tamanho de um texto  len de lenght

tamanho = len(email)
print(tamanho)

#trocar pedaço do email
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "guilherme fontoura"
print(nome.capitalize()) #primeira letra maiuscula
print(nome.title())# primeira letra de cada palavra maiuscula

#formatações especiais transformam um número em texto, não deixando mais calcular estes valores, utilizar direto no print  2500,00 deixar ele em float
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:.2f}\nCusto: {custo}\nLucro: {lucro}")  # \n para pular a linha (função do enter)
print(f"Margem: {margem:.0%}") #margem de 0.3 fica 30%

# exercicios


