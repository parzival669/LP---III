import random

def embaralhador(palavra):

    tamanho = len(palavra)

    lista = list(range(0,tamanho))
    for i in range (tamanho):
        numero_aleatoria = random.choice(lista)
        print (palavra[numero_aleatoria], end='')
        lista.remove(numero_aleatoria)


if __name__ == "__main__":
    while True:  
        palavra = input('\nPalavra : ').upper()
        embaralhador(palavra)