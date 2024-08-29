"""Questão 2 - Matriz de Combinações
A conhecida fórmula da análise combinatória:
(m,r) = m!/(m-r)!r!
nos diz quantas são as combinações de m objetos tomados r a r; no entanto, ela não diz como encontrar as tais combinações A seguir damos uma fórmula que cumpre essa finalidade.
A matriz de combinações e a fórmula geratriz são vistas a seguir:
Aij = 1, se i / 2^j é ímpar; 0, se i / 2^j é par. 
Vai entrar uma lista e um valor do número de combinações:
ex.: {a,b,c,d} e valor = 3
{{a,b,c},{a,b,d},{b,c,d},...}"""
import numpy as np
from math import floor

def MATRIZ_COMBINA(n):
    m = np.zeros((2**n, n), dtype=int) #Cria a matriz cheia de zeros com dimensão 2^n x n
    
    for i in range(2**n): #linha - como na fórmula passada tinha 2^n-1, mas no python já exclui o último termo, logo apenas colocar 2^n e equivale a 2^n-1 da fórmula
        for j in range(n): #coluna - como na fórmula passada tinha n-1, mas no python já exclui o último termo, logo apenas colocar n e equivale a n-1 da fórmula
            if floor(i / 2**j) % 2 == 0:
                m[i, j] = 0
            else:
                m[i, j] = 1
    
    return print(m)

# Exemplo igual do pdf
n = 5
MATRIZ_COMBINA(n)