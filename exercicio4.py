#quebrando um número

import math

x = float(input("Digite um numero real: "))
y = int(x)
z = math.trunc(x)

print("Numero inteiro: {}".format(y))
print("Numero inteiro: {}".format(z))