s = 0
for c in range(0, 4):
    n = int(input("Digite o valor: "))
    s = s + n
print(s)

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passos: "))

for d in range (i, f+1, p):
    print(d)