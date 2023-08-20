def main():
    n = int(input())

    for _ in range(n):
        larg, x = map(int, input().split())
        comandos = input()

        minimo, maximo = x, x
        for char in comandos:
            if char == 'E':
                x -= 1
            elif char == 'D':
                x += 1
            
            if x < minimo:
                minimo = x
            elif x > maximo:
                maximo = x
        
        print(len(range(minimo, maximo + 1)))


if __name__ == '__main__':
    main()