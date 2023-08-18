n = int(input())

for _ in range(n):
    linhas = [input() for _ in range(n)][::2] 
    
    for simbolo in ['X', 'O']:
        horizontais = any([linha[0] == linha[2] and linha[2] == linha[4] and linha[0] == simbolo for linha in linhas])
        verticais = any([x == y and y == z and x == simbolo for x, y, z in zip(*linhas)])
        diagonais1 = linhas[0][0] == linhas[1][2] and linhas[1][2] == linhas[2][4] and linhas[0][0] == simbolo
        diagonais2 = linhas[0][4] == linhas[1][2] and linhas[1][2] == linhas[2][0] and linhas[2][0] == simbolo

        if horizontais or verticais or diagonais1 or diagonais2:
            print(f"{simbolo} ganhou!")
            break
    else:
        print("Continue jogando!")