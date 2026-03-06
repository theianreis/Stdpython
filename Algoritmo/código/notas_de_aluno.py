n = int(input("Digite a quantidade de alunos: "))

array_nota = []

for _ in range(n):
    m=int(input("Quantidade de notas: "))
    array_nota.append(m)

print(array_nota)

array_nota_ordenador = sorted(array_nota,reverse=True)

print(array_nota_ordenador)


contador = 0
for i in range(len(array_nota)):
    if array_nota[i] != array_nota_ordenador[i]:
        contador += 1

print(contador)