palavras = []


for i in range(3):

	palavras.append(input())

if palavras[0] == "vertebrado":
	if palavras[1] == "ave":
		if palavras[2] == "carnivoro":
			animal = "aguia"
		else:
			animal = "pomba"
		
	else:
		if palavras[2] == "onivoro":
			animal = "homem"
		else:
			animal = "vaca"

else:

	if palavras[1] == "inseto":
		if palavras[2] == "hematofago":
			animal = "pulga"
		else:
			animal = "lagarta"

	else:
		if palavras[2] == "hematofago":
			animal = "sanguessuga"
		else:
			animal = "minhoca"



print(animal)