faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
print(faturamento)
print(lucro)

margem_lucro = lucro / faturamento
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)
#Mod resto da divisão (%)
#print(10 % 3) = 1
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12) #int, pega só a parte inteira de um número
print(tempo_em_anos)
print(tempo_em_meses % 12)

numero = 123.9
print(round(numero))# Round, arredonda o número decimal

#faturamento = 139_018_182 #dicao visual com _