a = int(input())
k = 0
tmp_s = 0

while a > tmp_s:
    k += 1
    tmp_s += k

k -= 1
y = tmp_s - a
x = k - y

if k % 2 == 1:
    print(f'{x+1}/{y+1}')
else:
    print(f'{y+1}/{x+1}')

