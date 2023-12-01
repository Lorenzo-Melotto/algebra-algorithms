import sys

def bezout(a: int, b: int) -> tuple[int, int, int]:
    """Calcola d=as+bt dove d=MCD(a, b) e restituisce una tupla `(d, s, t)`"""
    r: int = a
    r1: int = b
    u: int = 1
    v: int = 0
    u1: int = 0
    v1: int = 1
    r_tmp: int = 0
    u_tmp: int = 0
    v_tmp: int = 0
    while r1 != 0:
        q: int = r // r1
        r_tmp, u_tmp, v_tmp = r, u, v
        r, u, v = r1, u1, v1   
        r1 = r_tmp - q * r1
        u1 = u_tmp - q * u1
        v1 = v_tmp - q * v1
    return (r, u, v)

def main():
    args: list[str] = sys.argv

    if len(args) < 3:
        print("Usage: python bezout.py a b")
        exit(1)

    a: int = 0
    b: int = 0

    try:
        a = int(args[1])
        b = int(args[2])
    except ValueError as e:
        print(f"Errore: {e}")
        exit(1)
    
    # if b > a:
    #     a, b = b, a

    r, u, v = bezout(a, b)
    print(f"{r} = {a} * {u} + {b} * {v}")
    print(f"L'inverso moltiplicativo di {a} è {u % a} in Z_{a}")
    print(f"L'inverso moltiplicativo di {b} è {v % a} in Z_{a}")

if __name__ == "__main__":
    main()