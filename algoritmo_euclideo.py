import sys

def MCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def MCD_ext(a: int, b: int) -> int:
    """Calcola MCD(`a`, `b`) e stampa ogni risultato intermedio su stdout"""
    while True:
        rem = a % b
        q = (a - rem) // b
        print(f"{a} = {q} * {b} + {rem}")
        a, b = b, rem
        if b == 0: break
    return a

def main():
    args: list[str] = sys.argv
    if len(args) < 3:
        print("Usage: python Algoritmo_Euclideo.py <n> <m>")
        exit(1)

    a: int = 0
    b: int = 0
    try:
        a = int(args[1])
        b = int(args[2])
    except ValueError as e:
        print(f"Errore: {e}")
        exit(1)

    # strip out sign
    if a < 0: a = -a
    if b < 0: b = -b

    if b > a:
        a, b = b, a
    
    print(f"MCD({a}, {b}) = {MCD_ext(a, b)}")

if __name__ == "__main__":
    main()