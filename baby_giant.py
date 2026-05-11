import math
from utils import mod_inv

BRUTE_THRESHOLD = 1000


def brute_force(g, h, p, n, verbose=False):
    val = 1
    for x in range(n):
        if val == h % p:
            if verbose:
                print(f"    [перебор] нашли x={x}")
            return x
        val = val * g % p
    return None


def bsgs(g, h, p, n, verbose=False):
    if n <= BRUTE_THRESHOLD:
        if verbose:
            print(f"    [метод: перебор, порядок={n} <= {BRUTE_THRESHOLD}]")
        return brute_force(g, h, p, n, verbose)

    if verbose:
        print(f"    [метод: Шенкса (BSGS), порядок={n} > {BRUTE_THRESHOLD}]")

    m = math.isqrt(n) + 1

    # baby steps
    table = {}
    val = 1
    for j in range(m):
        table[val] = j
        val = val * g % p

    if verbose:
        print(f"    [bsgs] m={m}, baby steps посчитаны ({len(table)} шт)")

    # giant steps
    g_inv_m = pow(mod_inv(g, p), m, p)
    cur = h % p
    for i in range(m):
        if cur in table:
            x = (i * m + table[cur]) % n
            if verbose:
                print(f"    [bsgs] коллизия i={i} j={table[cur]}, x={x}")
            return x
        cur = cur * g_inv_m % p

    return None