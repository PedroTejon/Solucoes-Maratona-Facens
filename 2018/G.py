def main():
    i = int(input())

    for _ in range(i):
        entrada = input()
        
        count = 0
        while '-' in entrada:
            if entrada[0] == '+':
                index_f = entrada.index('-') if '-' in entrada else len(entrada)
                entrada = entrada.replace('+', '-', index_f)
            else:
                index_f = entrada.index('+') if '+' in entrada else len(entrada)
                entrada = entrada.replace('-', '+', index_f)
            
            count += 1
        
        print(count)


if __name__ == '__main__':
    main()