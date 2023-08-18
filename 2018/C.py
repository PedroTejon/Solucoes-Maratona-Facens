n = int(input())

for _ in range(n):
    qnt = int(input())
    figs = list(map(int, input().split()))
    figs.sort()
    print(' '.join(map(str, sorted(figs))))