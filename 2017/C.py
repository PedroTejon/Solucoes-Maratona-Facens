while True:
    n = int(input())
    if n < 0:
        break

    for i in range(n):
        for j in range(i):
            print(((1 * i - j) * (1 * j - i)) + 1, end=" ")
        print()