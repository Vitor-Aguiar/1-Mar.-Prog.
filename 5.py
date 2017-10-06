numeros = []
for i in range(5):

	numeros.append(int(input()))

cont = 0

for i in numeros:
	if i % 2 == 0:
		cont += 1

print(str(cont),"valores pares")