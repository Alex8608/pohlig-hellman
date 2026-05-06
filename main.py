import sys
from pohlig_hellman import pohlig_hellman


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python main.py <g> <h> <p>")
        print("Пример: python main.py 2 8 11")
        sys.exit(1)

    g, h, p = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    pohlig_hellman(g, h, p, verbose=True)