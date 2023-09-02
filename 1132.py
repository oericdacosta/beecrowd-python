x = int(input())
y = int(input())
somatorio = sum(i for i in range(x, y+1) if i % 13 != 0) if y > x else sum(i for i in range(y, x+1) if i % 13 != 0)
print(somatorio)
