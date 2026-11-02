import math

def calcular_cabo(distanias):
    total = 0
    for d in distanias:
        total += d
    margem = total * 0.10
    resultado = total + margem
    return math.floor(resultado)

distancias = [2, 3, 5, 4]
print(calcular_cabo(distancias))