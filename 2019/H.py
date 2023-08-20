from math import sqrt

def main():
    i = int(input())
    for _ in range(i):
        b, c = map(int, input().split())

        print(f'{sqrt((b ** 2) + (c ** 2)):.0f}')


if __name__ == '__main__':
    main()