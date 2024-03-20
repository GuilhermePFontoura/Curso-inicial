vendas = [100, 50, 130, 80, 120, 200]

print(vendas[-1]) 

total_vendas = sum(vendas) #sum, soma as vendas da lista
print(total_vendas)
quantidade = len(vendas) #len verifica quantos itens tem dentro da lista
print(quantidade)
valor_max = max(vendas)#maior venda
valor_min = min(vendas)#menor venda
print(valor_max, valor_min)

posicao = vendas.index(130) #index para descobrir a posição do item
print(posicao)

print(vendas[:2]) #mostrar até o indice 2
print(sum(vendas[:2])) #somar até o indice 2


produtos = ["iphone", "ipad", "airpod"]

print("iphone" in produtos) #in verifica se contém o item solicitado

precos = [4000, 8000, 2000]
novo_preco = precos[0] * 1.1
precos[0] = novo_preco
print(precos)

