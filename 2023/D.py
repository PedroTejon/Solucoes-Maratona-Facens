def main():
    i = int(input())

    for _ in range(i):
        n = int(input())

        menor_t_prim = 999999999
        menor_t_segu = 999999999
        menor_t_both = 999999999

        for _ in range(n):
            tempo, livro = input().split()
            tempo = int(tempo)
            
            if livro == '10' and menor_t_prim > tempo:
                menor_t_prim = tempo
            if livro == '01' and menor_t_segu > tempo:
                menor_t_segu = tempo
            if livro == '11' and menor_t_both > tempo:
                menor_t_both = tempo

        if menor_t_both < menor_t_prim + menor_t_segu:
            print(menor_t_both)
        else:
            print(menor_t_prim + menor_t_segu)

        



if __name__ == '__main__':
    main()