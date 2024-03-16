import matplotlib.pyplot as plt
from sympy import symbols, solve, evalf

A, r, d = symbols('A r d')

C2 = r * (A*(1-d*A)/(1-r))
A1 = C2 + A * (1-d*A)

expr = r * A + A1 *(1-d*A1)
sol = solve(expr, A)
print(sol)


a = []
c = []
r_val =1.1
d_val = 1
a_0 = sol[0].as_real_imag()[0].evalf(subs={r:r_val, d:d_val})
c_0 = C2.evalf(subs={r:r_val, d:d_val, A:a_0})
a.append(a_0)
print(a_0)
c.append(c_0)
print(c_0)

n = 100
for i in range(n):
    a_n = max(c[-1] + a[-1]* (1-d_val * a[-1]),0)
    a.append(a_n)
    c.append(a[-2]*r_val)

plt.plot(a, label='a')
plt.plot(c, label='c')
plt.legend()
plt.savefig('Exc1_sol3.png')
plt.show()

