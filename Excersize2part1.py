import matplotlib.pyplot as plt
from sympy import symbols, solve, evalf

delta_vec = [0.5, 1, 11/10]
c_0 = [0,0,0 ]
c_1 = []
c_2 = []
for delta in delta_vec:
    if delta != 1:
        c_temp = (-1 + (1+4*delta - 4*delta**2)**0.5)/(2-2*delta)
        c_1.append(c_temp)
        c_temp = (-1 - (1+4*delta- 4*delta**2)**0.5)/(2-2*delta)
        c_2.append(c_temp)
    else:
        c_1.append(9999999999)
        c_2.append(9999999999)
print('c0: ')
print(c_0)
print('c1: ')
print(c_1)
print('c2: ')
print(c_2)
c, dt = symbols('c dt')


for i,delta in enumerate(delta_vec):
    equation = c ** 2 / (1 + c ** 2) - delta * c / (1 + c)
    derivative = equation.diff(c)

    print('delta, c ')
    print(delta, c_2[i])

    print('sol')
    print(derivative.evalf(subs={c:c_2[i]}))

##### Ex 2.4
import matplotlib.pyplot as plt
from sympy import symbols, solve, evalf

c, dt = symbols('c dt')
c_new = c +dt *(c ** 2 / (1 + c ** 2) -  c / (1 + c))

c_0 = [0.9,0.1, 1.1]
c1 = [c_0[0]]
c2 = [c_0[1]]
c3 = [c_0[2]]
t = 1
for i in range(1000):

    c2.append(c_new.evalf(subs={c:c2[i], dt:t}))
    c3.append(c_new.evalf(subs={c:c3[i], dt:t}))
plt.plot(c2, label='c2 = 1')
plt.plot(c3, label='c3 = 1.1')

plt.xlabel('time steps ($\Delta t = 1$, arbitrary units)')
plt.ylabel('concentration (arbitrary units)')
c2 = [c_0[1]]
plt.legend()
plt.savefig('Exc2_sol4_diverge.png')
plt.show()
t = 0.1
for i in range(200):
    c1.append(c_new.evalf(subs={c:c1[i], dt:t}))
    c2.append(c_new.evalf(subs={c:c2[i], dt:t}))

plt.plot(c1, label='c1 = 0.9')
plt.plot(c2, label='c2 = 1')
plt.xlabel('time steps ($\Delta t = 0.1$, arbitrary units)')
plt.ylabel('concentration (arbitrary units)')
plt.legend()
plt.savefig('Exc2_sol4.png')
plt.show()
