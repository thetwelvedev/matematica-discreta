"""Questão 3 - Fórmulas da Soma de inteiros elevado a m 
Onde temos as seguintes fórmulas:
m = 1 -> n(n-1)/2
m = 2 -> n(n-1)(2n+1)/6
m = 3 -> n²(n-1)²/4
Então a saída tem que ser uma fórmula dependendo do valor de m.
"""
import sympy as sp

def a(m, j):
    """Calcula a fórmula a(m-j) para um dado j."""
    n = sp.symbols('n')
    termo = sum((-1)**k * sp.binomial(j, k) * (1 - k + j)**m for k in range(j + 1))
    return termo

def soma_inteiros_elevados(m):
    """Calcula a fórmula 1^m + 2^m + ... + n^m usando a fórmula fornecida."""
    n = sp.symbols('n')
    resultado = 0
    for j in range(m + 1):
        resultado += sp.binomial(m, j + 1) * a(m - j, j)
    return sp.simplify(resultado)

# Testando para diferentes valores de m
m_values = [1, 2, 3]
for m in m_values:
    resultado = soma_inteiros_elevados(m)
    print(f"Para m = {m}: {resultado}")

