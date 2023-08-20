from math import trunc


def coords_to_time(coords):
    hours, coords = coords.split('g', maxsplit=1)
    minutes, coords = coords.split('m', maxsplit=1)
    seconds, coords = coords.split('s', maxsplit=1)
    hours, minutes, seconds = map(int, [hours, minutes, seconds])

    minutes += seconds / 60
    hours += minutes / 60

    if coords[-1] == 'W' or coords[-1] == 'S':
        inteiros, decimais = str(-hours).split('.')
        decimais = decimais[:2] if len(decimais) > 2 else f'{decimais:0<2}'
        return f'{inteiros}.{decimais}'
    else:
        inteiros, decimais = str(hours).split('.')
        decimais = decimais[:2] if len(decimais) > 2 else f'{decimais:0<2}'
        return f'{inteiros}.{decimais}'
    


def main():
    while True:
        i = int(input())
        if i == 0:
            break

        for _ in range(i):
            coordsV, coordsH = input().split()

            print(f'{coords_to_time(coordsV):} {coords_to_time(coordsH)}')


if __name__ == '__main__':
    main()
