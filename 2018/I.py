def main():
    n = int(input())

    for _ in range(n):
        tam, qntd = map(int, input().split())
        chamadas = [input() for i in range(qntd)]

        falha = False
        for i, chamada in enumerate(chamadas[:-2]):
            for chamada2 in chamadas[i + 1:]:
                count = tam
                chars = []
                chars2 = []
                for char in range(tam):
                    if chamada[char] == chamada2[char]:
                        count -= 1
                    chars.append(chamada[char])
                    chars2.append(chamada2[char])
                if count < 2 or len(set(chars)) != len(chamada) or len(set(chars2)) != len(chamada2):
                    falha = True
                    break
            if falha:
                print("FALHA")
                break
        else:
            print("OK")


if __name__ == '__main__':
    main()