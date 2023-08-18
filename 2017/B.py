while True:
    n = int(input())
    if n == 0:
        break
    
    cadeia = input().replace('A', '@').replace('S', '$').replace('E', '3').replace('I', '!').replace('O', '0').replace(' ', '#')
    if n > 26:
        print('ERRO')
        continue

    cadeiaN = ''
    for char in cadeia:
        posicao = ord(char) - 65 + n
        if char.isalpha():
            cadeiaN += 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'[posicao]
        else:
            cadeiaN += char

    print(cadeiaN)
