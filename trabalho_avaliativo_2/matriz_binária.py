from math import floor

def matriz_binaria(n):
    m = [[0 for x in range(n)] for x in range(2**n)] # forma a matriz / List Comprehension
    soma = 0
    for i in range(2**n):
        for j in range(n):
            if floor(i / 2**j) % 2 == 0:
                m[i][j] = 0
            else:
                m[i][j] = 1
        
    return print(m)


matriz_binaria(4)