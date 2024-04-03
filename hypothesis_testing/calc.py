import math
# Middle
# lam = 1 / 20
# Begin
# lam = 1 / 10
# End
lam = 1 / 70

mu = 1 / 30
P = lam / mu
n = 3
p0 = 0
nf = math.factorial(n)
print(P / n)
for i in range(n + 1):
	p0 += (P ** i) / math.factorial(i) 
p0 += (P ** (n + 1)) / nf / (n - P)
p0 = p0 ** (-1)
print(p0)
L = n * (P ** (n + 1)) * p0 / nf / ((n - P) ** 2)
print((L + P) / lam)
print(L)
