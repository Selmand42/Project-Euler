# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143.

from math import isqrt

def check_prime(x):
	for i in range(2, isqrt(x) + 1):
		if x % i == 0:
			return False
	return True

for i in range(isqrt(600851475143) + 1, 1, -1):
	if 600851475143 / i % 1 == 0 and check_prime(i):
		print(i)
		break


