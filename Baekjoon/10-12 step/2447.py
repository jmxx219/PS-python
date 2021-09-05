def get_stars(star):
    matrix = []
    for i in range(3 * len(star)):
        x = star[i % len(star)]
        if i // len(star) == 1:
            matrix.append(x + " " * len(star) + x)
        else:
            matrix.append(x * 3)
    return matrix


n = int(input())
stars = ["***", "* *", "***"]
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    stars = get_stars(stars)

for star in stars:
    print(star)

