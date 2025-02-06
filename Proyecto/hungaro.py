import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    cost_matrix = np.array(cost_matrix)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    return row_ind, col_ind, total_cost

cost_matrix = [
    [4, 2, 8],
        [2, 3, 6],
        [5, 7, 2]
]

row_indices, col_indices, total_cost = hungarian_algorithm(cost_matrix)

print("Asignaciones (i, j):")
for i, j in zip(row_indices, col_indices):
    print(f"Agente {i} -> Tarea {j}")

print(f"Costo total: {total_cost}")









