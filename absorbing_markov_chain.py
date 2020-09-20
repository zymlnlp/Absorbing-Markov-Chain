from fractions import Fraction as frac

def gauss_jordan_elim(A):
    # First convert to row-echelon form
    for row_count in range(len(A)):

        col_count = row_count

        # find the maximum value in the current column
        curr_col = [abs(x[col_count]) for x in A[row_count:]]
        max_num_col = max(curr_col)  # maximum value
        max_num_col_pos = curr_col.index(max_num_col)  # the position of maximum value

        # swap this row with the row where the maximum value exists
        A[row_count], A[col_count + max_num_col_pos] = A[col_count + max_num_col_pos], A[row_count]

        # reduce the pivot of this row to 1
        if A[row_count][col_count] == 0:
            continue
        A[row_count] = [x / A[row_count][col_count] for x in A[row_count]]

        # convert the below row of this column to 0
        for row_count2 in range(row_count + 1, len(A)):
            if A[row_count2][col_count] == 0:
                continue

            w1 = A[row_count2][col_count] / A[row_count][col_count]

            for i in range(len(A[row_count2])):
                A[row_count2][i] = A[row_count2][i] - w1 * A[row_count][i]

    # Second convert to reduced row-echelon form
    for row_count in range(len(A)):
        col_count = row_count

        if row_count == 0:
            continue

        for count, num in enumerate(A[row_count]):

            if num == 1:
                for recall_count in range(1, row_count + 1):
                    if A[row_count - recall_count][count] != 0:

                        w2 = A[row_count - recall_count][count] / A[row_count][count]
                        for i in range(len(A[0])):
                            A[row_count - recall_count][i] = A[row_count - recall_count][i] - w2 * A[row_count][i]

                break

    return A


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


def statndard_form(m):
    absorb_state = []
    transit_state = []
    for index, row in enumerate(m):
        if row.count(0) == len(m[0]):
            absorb_state.append(index)
        else:
            transit_state.append(index)
    final_state = transit_state + absorb_state

    final = []
    for i, index1 in enumerate(final_state):
        final.append([])
        for index2 in final_state:
            final[i].append(m[index1][index2])
        total = sum(m[index1])
        if total != 0:
            for w in range(len(final_state)):
                final[i][w] = frac(final[i][w], total)

    return final, len(transit_state)


def solution(m):
    row_len, col_len = len(m), len(m[0])

    m, transit_len = statndard_form(m)

    Q, R = QR_decompose(m, transit_len, col_len)

    I = identity_matrix(transit_len)
    S = subtraction(I, Q)

    for i in range(transit_len):
        S[i] = S[i] + I[i]

    K = inverse_matrix(S, transit_len)
    print(K)
    prob = dot_product(K, R)[0]
    prob = common_denominator(prob)
    return prob
