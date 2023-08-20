def main():
    i = int(input())

    for _ in range(i):
        doador, receptor = input().split()
        
        doador_tipo = doador[0] if len(doador) == 2 else doador[0:2]
        doador_sinal = doador[1] if len(doador) == 2 else doador[2]
        receptor_tipo = receptor[0] if len(receptor) == 2 else receptor[0:2]
        receptor_sinal = receptor[1] if len(receptor) == 2 else receptor[2]

        if receptor_sinal == '-':
            if (doador_tipo in receptor_tipo or doador_tipo == 'O') and doador_sinal == '-':
                print('sim')
            else:
                print('nao')
        elif receptor_sinal == '+':
            if (doador_tipo in receptor_tipo or doador_tipo == 'O'):
                print('sim')
            else:
                print('nao')


if __name__ == '__main__':
    main()