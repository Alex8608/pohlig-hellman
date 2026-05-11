def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inv(a, m):
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError(f"gcd({a}, {m}) = {g}, обратного не существует")
    return x % m

def factorize(n):
    res = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            res[d] = res.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        res[n] = 1
    return res

def euler_phi(n):
    n_factors = factorize(n)
    result = n
    for p in n_factors:
        result -= result // p
    phi_factors = factorize(result)
    return result, phi_factors

def element_order(g, phi, factors, p):
    ord_g = phi
    for q in factors:
        while ord_g % q == 0 and pow(g, ord_g // q, p) == 1:
            ord_g //= q
    return ord_g