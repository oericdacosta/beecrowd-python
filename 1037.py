num = float(input())

if num >= 0 and num <= 25:
    print("intervalo [0,25]")
elif num > 25 and num <= 50:
    print("intervalo (25,50]")
elif num > 50 and num <= 75:
    print("intervalo (50,75]")
elif num > 75  and num <= 100:
    print("intervalo (75,100]")
else:
    print("Fora de intervalo")