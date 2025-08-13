#exercicio para criar um programa que leia algo do teclado e identifique o tipo do dado

n = input('digite algo: ')

if n.isnumeric() == True:
    print('É um numero!')
else:
    print('não é um numero')