from fractions import Fraction as frac
from Gauss_Jordan_Elimination import gauss_jordan_elim
from Standard_Form import standard_form


def inverse_matrix(A, transit_len):
    K = gauss_jordan_elim(A)
    new_K = []
    for row in K:
        new_K.append(row[transit_len:])
    return new_K


def dot_product(M1, M2):
    product = []
    for i in range(len(M1)):
        product.append([])
        R1 = M1[i]
        for i2 in range(len(M2[0])):
            R2 = [r[i2] for r in M2]
            product[i].append(sum(x[0] * x[1] for x in zip(R1, R2)))
    return product


def subtraction(a, b):
    k = []
    for c in range(len(a)):
        k.append([])
        for r in range(len(a)):
            k[c].append(a[c][r] - b[c][r])
    return k


def identity_matrix(transit_len):
    I = []

    for r in range(transit_len):
        I.append([])
        for c in range(transit_len):
            if r == c:
                I[r].append(frac(1, 1))
            else:
                I[r].append(frac(0, 1))
    return I


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def common_denominator(prob):
    lcm = int(prob[0].denominator)
    for num in prob[1:]:
        lcm = lcm * int(num.denominator) // gcd(lcm, int(num.denominator))

    new_list = []
    for num in prob:
        new_list.append(int(num * lcm))
    new_list.append(int(lcm))

    return new_list


def QR_decompose(m, transit_len, col_len):
    Q, R = [], []

    for r in range(transit_len):
        Q.append([])
        for c in range(transit_len):
            Q[r].append(m[r][c])

    for r in range(transit_len):
        R.append([])
        for c in range(transit_len, col_len):
            R[r].append(m[r][c])

    return Q, R


def solution(m):
    row_len, col_len = len(m), len(m[0])

    m, transit_len = standard_form(m)

    Q, R = QR_decompose(m, transit_len, col_len)

    I = identity_matrix(transit_len)
    S = subtraction(I, Q)

    for i in range(transit_len):
        S[i] = S[i] + I[i]

    K = inverse_matrix(S, transit_len)
    # print(K)
    prob = dot_product(K, R)[0]
    prob = common_denominator(prob)
    return prob


# default_matrix = [
#         [0, 1, 0, 0, 0, 1],
#         [4, 0, 0, 3, 2, 0],
#         [0, 0, 3, 0, 0, 0],
#         [0, 0, 5, 7, 0, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]

if __name__ == '__main__':

    with open("matrix_input.txt", "r") as f:
        input_matrix = [[int(num) for num in line.split(',')] for line in f]

    print("Note: If you want to modify the input matrix, please refers to 'matrix_input.txt' file. \n")
    print("Input Matrix for Testing: ")

    for s in input_matrix:
        print(*s)

    print("\nAbsorbing Markov Chain Solution: ")
    try:
        print(solution(input_matrix), "\n")
    except:
        print("Error: Please check the input matrix.")


