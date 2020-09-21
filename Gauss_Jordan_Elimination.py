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