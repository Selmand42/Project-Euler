# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

ans = 0
a, b = 1, 1

while b < 4 * (10 ** 6):
	b, a = a + b, b
	ans += b if b % 2 == 0 else 0

print(ans)
