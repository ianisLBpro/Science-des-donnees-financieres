# Nous voyons des manières de plus en plus efficaces de calculer les nombres de Fibonacci en Python


# Simple fonction récursive pour calculer le n-ième nombre de Fibonacci #
def fib_rec_py1 (n):
    if n < 2 :
        return n
    else : 
        return fib_rec_py1(n - 1) + fib_rec_py1(n - 2)
print('\n- Première méthode (attention aux nombres au dessus de 32, cela peut être très lent !)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
print(f'Le {n}ème nombre de Fibonacci est {fib_rec_py1(n)}\n')


# Fonction récursive mémorisée pour calculer le n-ième nombre de Fibonacci #
from functools import lru_cache as cache
@cache(maxsize=None)
def fib_rec_py2 (n):
    if n < 2 :
        return n
    else : 
        return fib_rec_py2(n - 1) + fib_rec_py2(n - 2)
print('\n- Deuxième méthode (plus rapide grâce à la mémorisation, mais s\'arrête à 998 pour cause de dépassement de la limite de récursion)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
print(f'Le {n}ème nombre de Fibonacci est {fib_rec_py2(n)}\n')


# Fonction itérative pour calculer le n-ième nombre de Fibonacci #
def fib_it_py(n):
    x, y = 0, 1
    for i in range(1, n + 1 ):
        x, y = y, x + y 
    return x
print('\n- Troisième méthode (très rapide et sans limite de récursion)')
n = int(input('Quel est le n-ième nombre de Fibonacci recherché ? '))
print(f'Le {n}ème nombre de Fibonacci est {fib_it_py(n)}\n')


# Extra : un générateur pour les nombres de Fibonacci jusqu'au n-ième terme #
def afficher_suite_fibonacci(n):
    """Affiche la suite de Fibonacci du 1er au n-ième terme"""
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input('Jusqu\'à quel terme voulez-vous afficher la suite ? '))
afficher_suite_fibonacci(n)
