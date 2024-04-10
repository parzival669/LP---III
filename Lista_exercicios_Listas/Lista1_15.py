i = 1
lista = []
while(1):
	coisa = int(input('Lista Eterna de Numeros - Coisa ' + str(i) + ': '))
	i += 1
	if(coisa == -1):
		print('Tchau')
		break
	else:
		lista.append(coisa)

print(lista)