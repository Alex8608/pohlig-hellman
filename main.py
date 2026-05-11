import sys
from pohlig_hellman import pohlig_hellman


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python main.py <g> <h> <p>")
        print("Пример: python main.py 2 8 11")
        sys.exit(1)

    g, h, p = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    h_mod = h % p

    if h_mod == 0:
        print("h = 0: решений нет")
        sys.exit(1)
    elif h_mod == 1:
        print("h = 1: x = 0 (g^0 = 1)")
        sys.exit(1)
    elif h_mod == p - 1:
        print(f"h = -1 = {p - 1}: тривиальный случай")
        sys.exit(1)

    pohlig_hellman(g, h, p, verbose=False)
