idade = []
altura = []
n_pessoa = 1
for i in range (5):
    print('\nPessoa ', n_pessoa)
    ida = int(input('Digite a idade: '))
    alt = int(input('Digite a altura: '))
    idade.append(ida)
    altura.append(alt)
    n_pessoa += 1

idade.reverse()
altura.reverse()
print('\nIdade', idade,'\nAltura', altura)