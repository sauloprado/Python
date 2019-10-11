lista = [500,23,45,78,12,35]

for i in range(len(lista)):

	menor = i

	for j  in range(len(lista)):

		if lista[j] < lista[menor]:
			menor = j
