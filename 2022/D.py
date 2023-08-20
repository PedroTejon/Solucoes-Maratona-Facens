def main():
    qntdP, qntdX = map(int, input().split())

    Ps = list(map(int, input().split()))

    for _ in range(qntdX):
        x = int(input())
        sum = 1
        for p in Ps:
            if (x - p) == 0:
                break
            sum *= (x - p)
        
        if sum == 0:
            print(0)
        elif sum > 0:
            print('+')
        else:
            print('-')


if __name__ == '__main__':
    main()