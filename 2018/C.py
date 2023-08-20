def main():
    n = int(input())

    for _ in range(n):
        qnt = int(input())
        figs = list(map(int, input().split()))
        figs.sort()
        print(' '.join(map(str, sorted(figs))))


if __name__ == '__main__':
    main()