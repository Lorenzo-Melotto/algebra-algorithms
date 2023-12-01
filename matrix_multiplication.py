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
    for i in range(rows):
        for j in range(cols):
            temp = 0.0
            for k in range(rows):
                temp += m1[i][k] * m2[k][j]
            res[i][j] = temp
    return res

def main():
    # matrix 1
    d1 = read_int("Number of rows of first matrix: ", min=1)
    d2 = read_int("Number of columns of first matrix: ", min=1)
    m1 = load_matrix(d1, d2)
    
    # matrix 2
    d1 = read_int("Number of rows of second matrix: ", min=1)
    d2 = read_int("Number of columns of second matrix: ", min=1)
    m2 = load_matrix(d1, d2)

    res = matrix_multiplication(m1, m2)

    # print the result
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(res[i][j], end="\t")
        print()

if __name__ == "__main__":
    main()