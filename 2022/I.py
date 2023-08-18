n = int(input())

for _ in range(n):
    num1, num2 = map(int, input().split())

    if num1 == num2:
        print('QUALQUER')
    elif num1 < num2:
        print('PRIMEIRO')
    else:
        print('SEGUNDO')