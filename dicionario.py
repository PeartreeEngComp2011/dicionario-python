dicionario = {"A":"André","B":"Beto", "C":"Carlos"}

print(dicionario["A"])

#Imprimir as chaves
for dgp in dicionario:
	print(dgp)

#Imprimir o dicionário
for dgp in dicionario:
	print(dicionario[dgp])

#Imprimindo os dois
for dgp in dicionario:
	print(dgp+"-"+dicionario[dgp])

#Outra forma de imprimir
for i in dicionario.items():
	print(i)

#Imprimindo valores
for i in dicionario.values():
	print(i)

#Imprimindo chaves
for i in dicionario.keys():
	print(i)