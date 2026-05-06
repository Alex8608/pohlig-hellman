from utils import factorize, element_order, mod_inv
from baby_giant import bsgs
from crt import crt


def ph_prime_power(g, h, p, prime, exp, verbose=False):
    n = element_order(g, p)
    q = prime ** exp

    gamma = pow(g, n // prime, p)

    x_acc = 0
    hk = h
    for k in range(exp):
        delta = pow(hk, n // prime**(k+1), p)
        if verbose:
            print(f"    [сведение к подгруппе] k={k}, delta={delta}")
        dk = bsgs(gamma, delta, p, prime, verbose=verbose)
        if dk is None:
            raise ValueError(f"bsgs не нашёл решение, delta={delta}")
        x_acc += dk * prime**k
        hk = hk * pow(mod_inv(g, p), dk * prime**k, p) % p

    return x_acc % q


def pohlig_hellman(g, h, p, verbose=False):
    print(f"\nDLP: {g}^x = {h} mod {p}")

    n = element_order(g, p)
    factors = factorize(n)

    print(f"ord(g) = {n} = {' * '.join(f'{q}^{e}' if e > 1 else str(q) for q, e in factors.items())}")

    if len(factors) == 1:
        prime, exp = list(factors.items())[0]
        if exp == 1:
            print(f"[пункт 1] порядок простое число ({n}) -> Шенкс или перебор")
        else:
            print(f"[пункт 2] порядок степень простого ({prime}^{exp}={n}) -> сведение к подгруппам")
    else:
        print(f"[пункт 3] порядок составное число -> редукция Полига-Хеллмана + КТО")

    remainders = []
    moduli = []

    for prime, exp in factors.items():
        q = prime ** exp
        if exp == 1:
            print(f"\nподзадача: порядок={prime} (простое) -> Шенкс/перебор")
        else:
            print(f"\nподзадача: порядок={prime}^{exp}={q} (степень простого) -> сведение к подгруппам")

        xi = ph_prime_power(g, h, p, prime, exp, verbose=verbose)
        print(f"  x = {xi} mod {q}")
        remainders.append(xi)
        moduli.append(q)

    if len(remainders) > 1:
        print(f"\nКТО: склеиваем {len(remainders)} подзадачи")
    x, M = crt(remainders, moduli)

    print(f"ответ: x = {x} mod {M}")
    print(f"проверка: {g}^{x} mod {p} = {pow(g, x, p)} (ожидается {h % p})")
    print("OK" if pow(g, x, p) == h % p else "ОШИБКА")

    return x