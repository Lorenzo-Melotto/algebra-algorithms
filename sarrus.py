def print_matrix(m: list[list[float]]) -> None:
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="\t")
        print()

def load_matrix(n: int, m: int) -> list[list[float]]:
    print(f"Insert your {n} x {m} matrix line by line:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Row {i+1}")
        for j in range(m):
            num = float(input(f" - Col {j+1}: "))
            row.append(num)
        matrix.append(row)
    print()
    return matrix

def sarrus(m: list[list[float]]) -> float:
    pos: float = 0
    neg: float = 0

    partial: float = 1
    partial *= m[0][0]
    partial *= m[1][1]
    partial *= m[2][2]

    pos += partial
    partial = 1

    partial *= m[1][0]
    partial *= m[2][1]
    partial *= m[0][2]

    pos += partial
    partial = 1

    partial *= m[0][1]
    partial *= m[1][2]
    partial *= m[2][0]

    pos += partial
    partial = 1

    partial *= m[2][0]
    partial *= m[1][1]
    partial *= m[0][2]

    neg -= partial
    partial = 1

    partial *= m[1][0]
    partial *= m[0][1]
    partial *= m[2][2]

    neg -= partial
    partial = 1

    partial *= m[2][1]
    partial *= m[1][2]
    partial *= m[0][0]

    neg -= partial
    return pos + neg

def main() -> None:
    m: list[list[float]] = load_matrix(3, 3)

    print(f"Matrix:")
    print_matrix(m)
    print()

    res: float = sarrus(m)
    print(f"The determinant is: {res}")

if __name__ == "__main__":
    main()
