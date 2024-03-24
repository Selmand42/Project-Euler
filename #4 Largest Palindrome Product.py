# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99
# Find the largest palindrome made from the product of two 3-digit numbers.

lpp = 0

def check_palindrome(x):
	return str(x) == str(x)[::-1]

for i in range(999, 99, -1):
	for j in range(999, i, -1):
		if i * j < lpp:	break

		if check_palindrome(i * j):
			lpp = max(lpp, i * j)

print(lpp)
