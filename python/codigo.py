faturamento = 1200 
custo = 770

novas_vendas = 300 #número inteiro
faturamento = faturamento + novas_vendas
taxa_imposto = 0.1 #float
mensagem = "O faturamento foi de" #string
teve_lucro = False  #boolean
imposto = taxa_imposto * faturamento
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)
