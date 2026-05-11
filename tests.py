import sys
from pohlig_hellman import pohlig_hellman
from generator import generate_task
from utils import euler_phi, element_order


def test_known():
    cases = [
        (2,  8,    11,   3,    "2^3 = 8 mod 11"),
        (2,  64,   101,  6,    "2^6 = 64 mod 101"),
        (6,  7531, 8101, 6689, "6^6689 = 7531 mod 8101"),
        (2,  pow(2, 1337, 10007), 10007, None, "x=1337, p=10007"),
    ]
    passed = 0
    for g, h, p, x_exp, desc in cases:
        x = pohlig_hellman(g, h, p)
        ok = pow(g, x, p) == h % p
        if x_exp is not None:
            ok = ok and (x == x_exp)
        print(f"{'OK' if ok else 'FAIL'} {desc}")
        passed += ok
    return passed, len(cases)


def test_random(count=20, bits=30):
    passed = 0
    for i in range(count):
        try:
            g, h, p, x_secret = generate_task(bits=bits)
            x = pohlig_hellman(g, h, p)
            ok = pow(g, x, p) == h % p
            print(f"{'OK' if ok else 'FAIL'} бит={p.bit_length()}, p={p}, x={x_secret}->{x}")
            passed += ok
        except Exception as e:
            print(f"FAIL исключение: {e}")
    return passed, count


def test_edge_cases():
    passed = 0
    total = 0

    # h = 1 -> x = 0
    p, g = 11, 2
    x = pohlig_hellman(g, 1, p)
    ok = pow(g, x, p) == 1
    print(f"{'OK' if ok else 'FAIL'} h=1: x={x}")
    passed += ok
    total += 1

    # x = 1 -> h = g
    p, g = 101, 2
    x = pohlig_hellman(g, g, p)
    phi, phi_f = euler_phi(p)
    ok = x % element_order(g, phi, phi_f, p) == 1
    print(f"{'OK' if ok else 'FAIL'} h=g: x={x}")
    passed += ok
    total += 1

    return passed, total


if __name__ == "__main__":
    print("=" * 50)
    print("ТЕСТ 1: известные ответы")
    print("=" * 50)
    p1, t1 = test_known()

    print()
    print("=" * 50)
    print("ТЕСТ 2: случайные задачи (20 шт, ~30 бит)")
    print("=" * 50)
    p2, t2 = test_random(count=20, bits=30)

    print()
    print("=" * 50)
    print("ТЕСТ 3: граничные случаи")
    print("=" * 50)
    p3, t3 = test_edge_cases()

    print()
    print("=" * 50)
    print(f"ИТОГО: {p1+p2+p3}/{t1+t2+t3}")
    sys.exit(0 if p1+p2+p3 == t1+t2+t3 else 1)