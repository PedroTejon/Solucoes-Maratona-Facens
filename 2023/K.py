def main():
    i = int(input())
    for _ in range(i):
        prim_part, segu_parte = input().split('mek')

        qntd = prim_part.count('a') * segu_parte.count('a')

        print(f'k{"a" * qntd}')


if __name__ == '__main__':
    main()