import random


def is_prime(n):
    # тест Миллера-Рабина
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in witnesses:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_task(bits=30):
    from utils import euler_phi, element_order

    while True:
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        n = 1
        while n.bit_length() < bits - 2:
            n *= random.choice(small_primes)
        p = n + 1

        if not is_prime(p):
            continue
        if p.bit_length() < bits - 2 or p.bit_length() > bits + 2:
            continue

        phi, phi_factors = euler_phi(p)

        for _ in range(100):
            g = random.randint(2, p - 1)
            ord_g = element_order(g, phi, phi_factors, p)
            if ord_g > 1:
                break
        else:
            continue

        x_secret = random.randint(1, ord_g - 1)
        h = pow(g, x_secret, p)
        return g, h, p, x_secret


if __name__ == "__main__":
    for bits in [20, 30, 50]:
        g, h, p, x = generate_task(bits=bits)
        print(f"{bits} бит: p={p}, g={g}, h={h}, x={x}")
        print(f"  проверка: {pow(g, x, p) == h}")