# Your code here
def matrix_builder(int):

    matrix = []

    for i in range(int):
        row = []
        for i in range(int):
            row.append(1)
        matrix.append(row)
    
    return matrix

print(matrix_builder(5))