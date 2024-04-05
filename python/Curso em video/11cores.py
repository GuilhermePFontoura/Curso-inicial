#Style: 0 (none) , 1 (negrito), 4 (sublinhado), 7(negativo)
#text: 30(branco), 31(vermelho), 32 (verde), 33(amarelo), 34 (azul), 35 (roxo), 36 (azul claro), 37 (cinza)
#back: 40,41,42,43,44,45,46,47 com as mesmas cores do texto
cores = {"verde":"\033[32m", 
         "azul":"\033[34m", 
         "limpa":"\033[m"} #sistema de cores
nome = "Guilherme"
print("\033[30;45;7m Ola Mundo\033[m")
a = 5
b = 8
print("A soma entre \033[31;1m{}\033[m e \033[36;1m{}\033[m é \033[35m{}\033[m !!!".format(a, b, a+b))
print("{}Meu nome é{} {}{}{}!!!".format(cores["verde"], cores["limpa"], cores["azul"], nome, cores["limpa"]))#usando lista de cores


