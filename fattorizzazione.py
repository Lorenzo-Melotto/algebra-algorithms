#!/usr/bin/python3
from sys import argv, stderr

def is_prime(n: int) -> bool:
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def factorize(num: int) -> list[int]:
    """Returns a list containing the factorization of `num`
    ```python
    factorize(7)  # returns [7]
    factorize(15) # returns [3, 5]
    factorize(8)  # returns [2, 2, 2]
    ```
    """
    factors: list[int] = []
    i: int = 2
    while num > 1:
        if is_prime(i) and num % i == 0:
            num //= i
            factors.append(i)
            i = 2
            continue
        i += 1
    return factors

def main() -> None:
    if len(argv) < 2:
        print(f"Usage: python fattorizzazione.py <n>")
        exit(1)

    num: int = 0
    try:
        num = int(argv[1])
    except ValueError as e:
        print(f"ERROR: {e}", file=stderr)
        exit(1)

    factors = factorize(num)
    print(f"Factorization of number {num}: {factors}")

if __name__ == "__main__":
    main()