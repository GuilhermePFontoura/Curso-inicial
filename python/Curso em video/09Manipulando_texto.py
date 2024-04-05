frase = "Curso em video python"
print(len(frase))#contar o numero de caracteres na frase
print(frase.count('o', 0, 13))#contar quantas letras o tem na frase entre posição 0 e 13
print(frase[2:9])#cortar a frase da posição 2 a 9
print(frase.find("deo"))#passa a posição da palavra deo
print(frase.find("Android"))#procura android na frase
print("Curso" in frase)#procura curso em frase e indica true ou false
print(frase.replace("python", "android"))#troca python por android nessa linha, para alterar na variavel precisa colocar frase = frase.replace
print(frase.upper())#coloca frase para maiusculo
print(frase.lower())#coloca em minusculo a frase
print(frase.capitalize())#coloca a primeira letra da frase em maiusculo e resto em minusculo
print(frase.title())#coloca a primeira letra de cada palavra da frase em maiusculo
print(frase.strip())#elimina espaços inuteis do inicio e fim da frase
print(frase.rstrip())#elimina espaços inuteis no lado direito da frase, poderia ser lstrip para remover do inicio
print(frase.split())#Divide a frase considerando os espaços, transformando em lista
print("-".join(frase.split()))#coloca - para separar as palavras
print("""Oi
      estou aprendendo python
      E posso divir o texto com 3 aspas """)
print(frase.upper().count("O"))#colocar mais de uma ação junto para a variavel.



