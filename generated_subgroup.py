#!/usr/bin/python3
import sys

def calc_generated_subgroup(n: int, mod: int) -> list[int]:
    res: list[int] = []
    for i in range(1, mod+1):
        tmp: int = (n**i) % mod
        res.append(tmp)
        if tmp == 1: break
    return res

def main() -> None:
    args: list[str] = sys.argv

    if len(args) < 3:
        print("Usage: python3 generated_subgroup.py <element> <group>")
        exit(1)

    try:
        num: int = int(args[1])
        modulo: int = int(args[2])
    except ValueError as e:
        print(f"ERROR: {e}")
        exit(1)

    res: list[int] = calc_generated_subgroup(num, modulo)
    print(f"{len(res)} elementi: {res}")

if __name__ == "__main__":
    main()
