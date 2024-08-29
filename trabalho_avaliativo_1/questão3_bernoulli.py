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

def faulhaber_formula(m):
    n = sp.Symbol('n', integer=True)
    sum_formula = 0
    
    for k in range(m + 1):
        bernoulli_term = sp.bernoulli(k)
        term = (bernoulli_term * sp.binomial(m + 1, k) * n**(m + 1 - k)) / (m + 1)
        sum_formula += term
    
    return sp.simplify(sum_formula)

# Exemplo de uso
m = int(input("Digite o valor da potência: "))
limpar_tela()
sp.pretty_print(faulhaber_formula(m))