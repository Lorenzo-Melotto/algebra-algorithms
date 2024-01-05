from utils import read_int

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

def matrix_multiplication(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    rows = len(m1)
    cols = len(m2[0])
    res = [[0.0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            temp = 0.0
            for cs in range(len(m1[0])):
                temp += m1[r][cs] * m2[cs][c]
            res[r][c] = temp
    return res

def print_matrix(m: list[list[float]]) -> None:
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="\t")
        print()

def main():
    
    # matrix 1
    d1: int = read_int("Number of rows of first matrix: ", min=1)
    d2: int = read_int("Number of columns of first matrix: ", min=1)
    m1: list[list[float]] = load_matrix(d1, d2)
    
    # matrix 2
    d1 = read_int("Number of rows of second matrix: ", min=1)
    d2 = read_int("Number of columns of second matrix: ", min=1)
    m2: list[list[float]] = load_matrix(d1, d2)
    
    print("Matrix 1: ")
    print_matrix(m1)
    
    print()
    
    print("Matrix 2:")
    print_matrix(m2)

    print()

    res: list[list[float]] = matrix_multiplication(m1, m2)

    # print the result
    print("Result:")
    print_matrix(res)

if __name__ == "__main__":
    main()
