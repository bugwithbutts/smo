import scipy.stats as st
def P(j):
	return st.expon.cdf(j, 0, 10)
file = open('../parsed_data/parsed', 'r')
a = 0.1
l1 = []
for i in file.readlines():
	l1.append(int(i[:-1]))
l1.sort()
l1 = l1[:100]
N = 10
mn = 1000000
mx = 0
l2 = []
lst = l1[0]
for i in l1:
	l2.append(i - lst)
	lst = i
l2 = l2[1:]
mn = min(l2)
mx = max(l2)
step = (mx - mn) / N
cnt = [0 for _ in range(N)]
for i in l2:
	for j in range(N):
		if mn + step * j < i and mn + step * (j + 1) >= i:
			cnt[j] += 1
Xi = 0
for i in range(N):
	tmp = P(mn + (i + 1) * step) - P(mn + i * step)
	# print(tmp)
	Xi += (cnt[i] - tmp * len(l2)) ** 2 / len(l2) / tmp
print(Xi)
print("should be >=")
print(st.chi2.ppf(1 - a, df = N - 1))
print("to cancel H0")