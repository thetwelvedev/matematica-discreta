import sympy as sp
# Discente: Victor Hugo Souza Costa 

def gerador_formula(m):
    n = sp.Symbol('n', integer=True)
    formula = 0

    for i in range(m+1):
        a = 0
        for j in range(i+1):
            a += (((-1)**j) * sp.binomial(i, j) *((1-j+i)**m))
        
        term = sp.binomial(n, i+1)*a
        formula += term
    return formula

m = int(input("Digite a potência: ")) 
formula = gerador_formula(m).simplify()
sp.pretty_print(formula)