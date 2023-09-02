s = 1
j = 2
for i in range(3, 40, 2):
    s += i/j
    j *= 2
print(f'{s:.2f}')