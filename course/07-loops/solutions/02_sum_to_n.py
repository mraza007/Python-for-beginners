"""Solution — Exercise 2: Sum from 1 to n."""

n = 10

total = 0
for number in range(1, n + 1):
    total += number

print(f"Sum 1 to {n} = {total}")
