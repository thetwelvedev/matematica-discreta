"""Questão 1 - Matriz da eletrônica Digital
A matriz que comparece na análise de circuitos em eletronica digital  a vista a seguir: 
Aij = 1, se i - 1 / 2**(N - j) e 0, se i - 1 / 2**(N - j). 
Acima temos uma fórmula que gera a matriz, N é o número de variáveis lógicas (na entrada do circuito). """
import numpy as np
from math import floor

def EXPORT_MED(n):
    m = np.zeros((2**n, n), dtype=int) #Cria a matriz cheia de zeros
    
    for i in range(1, 2**n + 1): #linha e tem que ser + 1 pois não conta o último valor 
        for j in range(1, n + 1): #coluna e tem que ser + 1 pois não conta o último valor
            if floor((i-1) / 2**(n-j)) % 2 == 0:
                m[i-1, j-1] = 0
            else:
                m[i-1, j-1] = 1
    
    return print(m)

# Exemplo de uso igual do pdf
n = 3
EXPORT_MED(n)