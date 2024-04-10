import math
vetor = [1,2,3,4,5,6,7,8,9,10]
raizes = []

cont = 0
for i in range(len(vetor)):
    raiz = math.sqrt(vetor[cont])
    raizes.append(raiz)
    cont += 1

print('\nRaizes:\n',raizes)
print('\nSoma:\n',sum(raizes))