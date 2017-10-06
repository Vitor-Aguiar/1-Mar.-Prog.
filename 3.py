vetor = [4.00,4.50,5.00,2.00,1.50]

numeros = input().split()

codigo = int(numeros[0])
quantidade = float(numeros[1])

total = vetor[codigo-1]*quantidade

print("Total: R$ %.2f" %total)