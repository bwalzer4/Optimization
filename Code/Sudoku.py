import numpy as np
import cvxpy as cp

# Initialize the starting board
init_board = np.array([[9, 0, 0, 0, 0, 0, 0, 0, 3],
                       [0, 0, 4, 0, 1, 0, 0, 7, 0],
                       [0, 5, 2, 0, 0, 6, 8, 0, 0],
                       [0, 0, 0, 0, 0, 4, 3, 0, 0],
                       [0, 6, 0, 0, 2, 0, 0, 8, 0],
                       [0, 0, 5, 9, 0, 0, 0, 0, 0],
                       [0, 0, 9, 1, 0, 0, 2, 5, 0],
                       [0, 2, 0, 0, 6, 0, 4, 0, 0],
                       [7, 0, 0, 0, 0, 0, 0, 0, 1]])

init_board

# Create the binary variables and a dummy variable x that doesn't really do anything
x = cp.Variable((9, 9))
b_1 = cp.Variable((9, 9), boolean=True)
b_2 = cp.Variable((9, 9), boolean=True)
b_3 = cp.Variable((9, 9), boolean=True)
b_4 = cp.Variable((9, 9), boolean=True)
b_5 = cp.Variable((9, 9), boolean=True)
b_6 = cp.Variable((9, 9), boolean=True)
b_7 = cp.Variable((9, 9), boolean=True)
b_8 = cp.Variable((9, 9), boolean=True)
b_9 = cp.Variable((9, 9), boolean=True)

# Create a list of each variable
b_list = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]

# Set up Constraints
constraints = [x >= 0]

for i, b in enumerate(b_list):
    indices = np.argwhere(init_board == i + 1)
    if len(indices) > 0:
        for (x, y) in indices:
            constraints += [b[x][y] == 1]

# Create constraints that each number can only show up once in a row or column
for b in b_list:
    for i in range(0, 9):
        constraints += [cp.sum(b[:, i]) == 1, cp.sum(b[i, :]) == 1]

# Create constraints that each number can only appear once in a 3x3 grid
for b in b_list:
    for i in range(0, 3):
        constraints += [cp.sum(b[0:3, i * 3:3 + i * 3]) == 1]
        constraints += [cp.sum(b[3:6, i * 3:3 + i * 3]) == 1]
        constraints += [cp.sum(b[6:9, i * 3:3 + i * 3]) == 1]

# Create constraints that only one number can appear in a cell
for i in range(0, 9):
    for j in range(0, 9):
        constraints += [cp.sum(b_1[i][j] + b_2[i][j] + b_3[i][j] +
                               b_4[i][j] + b_5[i][j] + b_6[i][j] +
                               b_7[i][j] + b_8[i][j] + b_9[i][j]) == 1]

# Set up the optimization problem, which doesn't really matter since we are just trying to find
# a feasible solution to the constraints

obj = cp.Minimize(cp.sum(x))

prob = cp.Problem(obj, constraints)

prob.solve()
print("Status:", prob.status)

# This prints out each of the binary variables
for i, b in enumerate(b_list):
    print('b_' + str(i + 1), b.value)

# Apply the acutal numbers to the binary variables i.e if b_2 == 1 in a cell then change value to 2,
# otherwise leave cell at 0
for i, v in enumerate(range(1, 10)):
    b_list[i] = b_list[i].value * v

# Create an empty baord then add all binary variables together
solved_sodoku = np.zeros((9, 9))
for b in b_list:
    solved_sodoku += b

solved_sodoku
