import random as rdm
from random import randint
import time

import pygame

print(rdm.randint(1,6))
print(randint(1, 6))

lista = [1, 2, 3, 4, 5, 6]
outra_lista = lista.copy()
rdm.shuffle(outra_lista)

print(lista)
print(outra_lista)

def fatorial(n):
    fat = 1
    for i in range(1, n, 1):
        fat += 1

    return fat

inicio = time.time()
fatorial(1000000)
print(f"Tempo decorrido: {time.time() - inicio:.2f}")