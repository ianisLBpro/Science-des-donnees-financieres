'''
Recherches_nb_premiers 

Rappelons qu'un nombre premier est un entier naturel positif supérieur 
à 1 qui n'est divisible que par 1 sans donner de reste ou par lui-même.

Plus on progresse dans la recherche de nombres premiers, 
plus les nombres deviennent grands, et plus la recherche devient longue. 

Nous allons voir comment trouver des nombres premiers en Python, 
et comment optimiser cette recherche avec des outils comme Numba.

Testez le nombre premier suivant pour réellement voir la différence de performance :
100109100129162907

'''


import time
import numba



# Fonction pour tester si un nombre est premier #
def is_prime(nb):
    if nb < 2: return False
    if nb == 2: return True
    if nb % 2 == 0: return False
    for i in range(3, int(nb ** 0.5) + 1, 2):
        if nb % i == 0: return False
    return True

# Préparation Numba (compilation JIT à vide, hors mesure)
is_prime_nb = numba.jit(is_prime)
is_prime_nb(2)




'''
Exercice 1 : Testez si un nombre est premier en Python et en Numba.
'''
nb = int(input('Quel nombre voulez-vous tester pour savoir s\'il est premier ? '))

print('Recherche si le nombre est premier en Python :')
start = time.time()
print(nb)
print(is_prime(nb))
print(f"Python pur : {time.time() - start:.6f} s\n")

print('Recherche si le nombre est premier en Numba :')
start = time.time()
print(nb)
print(is_prime_nb(nb))
print(f"Numba : {time.time() - start:.6f} s\n")




'''
Exercice 2 : Affichez les n premiers nombres premiers en Python et en Numba.
'''
nb_2 = int(input('Combien de nombres premiers voulez-vous afficher ? '))

print('\n Affichage des nombres premiers en Python :')
start = time.time()
count, n = 0, 2
while count < nb_2:
    if is_prime(n):
        print(n, end=' ')
        count += 1
    n += 1
print(f"\nPython pur : {time.time() - start:.6f} s")

print('\n Affichage des nombres premiers en Numba :')
start = time.time()
count, n = 0, 2
while count < nb_2:
    if is_prime_nb(n):
        print(n, end=' ')
        count += 1
    n += 1
print(f"\nNumba : {time.time() - start:.6f} s")