from utils import mod_inv


def crt(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m

    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * mod_inv(Mi, m)

    return x % M, M
