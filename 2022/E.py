from math import lcm


def main():
    i = int(input())

    for _ in range(i):
        qntdAmigos, qntdFatias = map(int, input().split())

        print(lcm(qntdAmigos, qntdFatias) // qntdFatias)


if __name__ == '__main__':
    main()
