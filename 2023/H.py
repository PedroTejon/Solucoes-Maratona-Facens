def main():
    i = int(input())

    for _ in range(i):
        xseA, yseA, xidA, yidA, xseB, yseB, xidB, yidB = map(int, input().split())

        larguraA = xidA - xseA
        alturaA = yseA - yidA
        areaA = larguraA * alturaA

        larguraB = xidB - xseB
        alturaB = yseB - yidB
        areaB = larguraB * alturaB

        if areaB > areaA or areaB == areaA:
            print('terreno B')
        else:
            print('terreno A')


if __name__ == '__main__':
    main()
