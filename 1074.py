for x in range(int(input())):
    num = int(input())
    if num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    elif num > 0 and num % 2 != 0:
        print('ODD POSITIVE')
    elif num < 0 and num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num < 0 and num % 2 != 0:
        print('ODD NEGATIVE')
    else:
        print('NULL')