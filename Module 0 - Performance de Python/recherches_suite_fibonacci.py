'''
Recherches_suite_fibonacci

La suite de Fibonacci est une séquence de nombres où chaque nombre est la somme des deux précédents.

Au départ on définit deux fois le chiffre 1, puis à partir du troisième terme, 
le nombre de Fibonacci suivant est la somme des deux précédents : 1, 1, 2, 3, 5, 8, 13, 21...

Voyons deux méthodes d'implémentation, une récursive et un itérative, et comparons leurs performances.
'''


import time



# Simple fonction récursive pour calculer le n-ième nombre de Fibonacci #
def fib_rec_py1 (n):
    if n < 2 :
        return n
    else : 
        return fib_rec_py1(n - 1) + fib_rec_py1(n - 2)

print('\n- Première méthode (attention aux nombres au dessus de 32, cela peut être très lent !)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
start = time.time()
result = fib_rec_py1(n)
print(f'Le {n}ème nombre de Fibonacci est {result}')
print(f'Temps : {time.time() - start:.6f} s\n')


# Fonction récursive mémorisée pour calculer le n-ième nombre de Fibonacci #
from functools import lru_cache as cache
@cache(maxsize=None)
def fib_rec_py2 (n):
    if n < 2 :
        return n
    else : 
        return fib_rec_py2(n - 1) + fib_rec_py2(n - 2)

print('\n- Deuxième méthode (plus rapide grâce à la mémorisation)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
start = time.time()
result = fib_rec_py2(n)
print(f'Le {n}ème nombre de Fibonacci est {result}')
print(f'Temps : {time.time() - start:.6f} s\n')


# Fonction itérative pour calculer le n-ième nombre de Fibonacci #
def fib_it_py(n):
    x, y = 0, 1
    for i in range(1, n + 1 ):
        x, y = y, x + y 
    return x

print('\n- Troisième méthode (très rapide et sans limite de récursion)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
start = time.time()
result = fib_it_py(n)
print(f'Le {n}ème nombre de Fibonacci est {result}')
print(f'Temps : {time.time() - start:.6f} s\n')


# Extra : un générateur pour les nombres de Fibonacci jusqu'au n-ième terme #
def afficher_suite_fibonacci(n):
    """Affiche la suite de Fibonacci du 1er au n-ième terme"""
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input('Jusqu\'à quel terme voulez-vous afficher la suite ? '))
start = time.time()
afficher_suite_fibonacci(n)
print(f'\nTemps : {time.time() - start:.6f} s')
