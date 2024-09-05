"""Questão 3 - Fórmulas da Soma de inteiros elevado a m 
Onde temos as seguintes fórmulas:
m = 1 -> n(n-1)/2
m = 2 -> n(n-1)(2n+1)/6
m = 3 -> n²(n-1)²/4
Então a saída tem que ser uma fórmula dependendo do valor de m.
"""
import sympy as sp
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def formula_PAM4(m):
    for j in range(m+1):
        a = 0
        for k in range(0, j+1):
            a += (((-1)**k) * sp.binomial(j, k) *((1-k+j)**m))
    return a
    
def formula_PAM5(m):
    n = sp.Symbol('n', integer=True)
    formula = 0
    for j in range(m+1):
        a = formula_PAM4(m)
        term = sp.binomial(n, j+1)*a
        formula += term
    return sp.simplify(formula)


# Exemplo de uso
m = int(input("Digite o valor da potência: "))
limpar_tela()
sp.pretty_print(formula_PAM5(m))