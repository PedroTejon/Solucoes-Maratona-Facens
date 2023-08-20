from math import lcm, gcd


def main():
    i = int(input())

    for _ in range(i):
        a, b, c, d = map(int, input().split())

        denominador = lcm(b, d)
        numerador = int(denominador / b * a) + int(denominador / d * c)

        simplificador = gcd(numerador, denominador)
    
        print(f'{numerador // simplificador}/{denominador // simplificador}')


if __name__ == '__main__':
    main()
