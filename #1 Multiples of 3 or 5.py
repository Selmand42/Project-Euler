# Find the sum of all the multiples of 3 or 5 below 1000.

ans = sum(i for i in range(2, 1000) if i % 3 == 0 or i % 5 == 0)
print(ans)
