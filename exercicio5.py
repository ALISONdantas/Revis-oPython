#calculando seno, cosseno e tangente

import math

x = float(input("Digite um angulo: "))
seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x))
tangente = math.tan(math.radians(x))

print("Seno: {}\nCosseno: {}\nTangente: {}".format(seno, cosseno, tangente))