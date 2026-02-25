
# Recherche de nombres premiers #
def is_prime(nb):
    if nb % 2 == 0: return False
    for i in range(3, int(nb ** 0.5) + 1, 2):
        if nb % i == 0: return False
    return True

nb = int(13)
print(nb)
print(is_prime(nb))


# Recherche de nombres premiers en numba #
import numba    
is_prime_nb = numba.jit(is_prime)

print(nb)
print(is_prime_nb(nb))
