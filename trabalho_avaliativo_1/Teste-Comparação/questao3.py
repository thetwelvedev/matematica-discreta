import sympy as sp

def gerador_formula(m):
    n = sp.Symbol('n', integer=True)
    formula = 0

    for j in range(m+1):
        a = 0
        for k in range(j+1):
            a += (((-1)**k) * sp.binomial(j, k) *((1-k+j)**m))
        
        term = sp.binomial(n, j+1)*a
        formula += term
    return sp.simplify(formula)

m = int(input("Digite a potência: ")) 
sp.pretty_print(gerador_formula(m))