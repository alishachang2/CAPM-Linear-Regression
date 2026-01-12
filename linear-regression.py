import csv


def transpose(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    transposed = []

    for col in range(COLS):
        new_row = []
        for row in range(ROWS):
            value = matrix[row][col]
            new_row.append(value)
        transposed.append(new_row)

    return transposed


def mat_mul(A, B):
    ROWS_A = len(A)
    COLS_A = len(A[0])
    ROWS_B = len(B)
    COLS_B = len(B[0])

    if COLS_A != ROWS_B:
        raise ValueError("A's columns must match B's rows")

    # Create result matrix filled with zeros
    result = []
    for _ in range(ROWS_A):
        new_row = []
        for _ in range(COLS_B):
            new_row.append(0)
        result.append(new_row)

    # Compute matrix product
    for i in range(ROWS_A):
        for j in range(COLS_B):
            running_sum = 0
            for k in range(COLS_A):
                left_value = A[i][k]
                right_value = B[k][j]
                product = left_value * right_value
                running_sum += product
            result[i][j] = running_sum

    return result


def invert_2x2(matrix):
    # Extract values
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    DET = a * d - b * c
    if DET == 0:
        raise ValueError("Singular matrix, cannot invert")

    inv = [[d / DET, -b / DET], [-c / DET, a / DET]]

    return inv


MKT_RF = []
RV_subt_rf = []
with open("DATA.csv", "r") as d:
    reader = csv.DictReader(d)
    for row in reader:
        MKT_RF.append(row["MKT_RF"])
        RV_subt_rf.append([float(row["RV-rf"])])

A = []
for num in MKT_RF:
    A.append([float(num), 1.0])

A_T = transpose(A)

# A_T * A
A_T_A = mat_mul(A_T, A)

# inverse of (A_T*A)
A_T_A_inv = invert_2x2(A_T_A)

# A_T * y
A_T_y = mat_mul(A_T, RV_subt_rf)

#  inv * (A_T * y)
weights = mat_mul(A_T_A_inv, A_T_y)
print(weights)
# beta
beta = weights[0][0]

# alpha
alpha = weights[1][0]
print(beta, alpha)
