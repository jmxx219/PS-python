n = int(input())
i = 2
r = int(n ** 0.5)

while i <= r:
    while n % i == 0:
        n //= i
        print(i)
    i += 1
if n > 1:
    print(n)
