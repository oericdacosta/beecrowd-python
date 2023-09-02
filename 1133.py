x = int(input())
y = int(input())
[print(i) for i in range(x+1, y) if i % 5 in (2, 3)] if y > x else [print(i) for i in range(y+1, x) if i % 5 in (2, 3)]