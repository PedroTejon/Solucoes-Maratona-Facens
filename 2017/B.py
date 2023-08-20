def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        cadeia = input().replace('A', '@').replace('S', '$').replace('E', '3').replace('I', '!').replace('O', '0').replace(' ', '#')
        if n > 26:
            print('ERRO')
            continue

        cadeia_nova = ''
        for char in cadeia:
            posicao = ord(char) - 65 + n
            if char.isalpha():
                cadeia_nova += 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'[posicao]
            else:
                cadeia_nova += char

        print(cadeia_nova)


if __name__ == '__main__':
    main()
