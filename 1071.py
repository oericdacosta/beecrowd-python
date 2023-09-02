x, y = int(input()), int(input())
somatorio = 0

if x > y:
    for num in range(y+1, x):
        if num % 2 != 0:    
            somatorio += num
else:
    for num in range(x+1, y):
        if num % 2 != 0:    
            somatorio += num

print(somatorio)