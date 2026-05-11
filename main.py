import sys
from pohlig_hellman import pohlig_hellman
from utils import euler_phi, element_order

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python main.py <g> <h> <p>")
        print("Пример: python main.py 2 8 11")
        sys.exit(1)

    g, h, p = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    h_mod = h % p

    if h_mod == 0:
        print("h = 0: решений нет")
        sys.exit(0)
    elif h_mod == 1:
        print("h = 1: x = 0 (g^0 = 1)")
        sys.exit(0)
    elif h_mod == p - 1:
        phi, phi_factors = euler_phi(p)
        n = element_order(g, phi, phi_factors, p)
        if n % 2 == 0:
            print(f"h = -1: x = {n // 2}")
        else:
            print("h = -1: решений нет (порядок g нечётный)")
        sys.exit(0)

    pohlig_hellman(g, h, p, verbose=False)
