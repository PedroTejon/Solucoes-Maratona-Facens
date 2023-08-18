def dfs(imports):
    visitados = set()
    stack = []
    
    for imp in imports:
        if imp in visitados:
            continue
        stack.append(imp)

        while stack:
            atual = stack.pop(0)

            if atual not in visitados:
                visitados.add(atual)
            
            for imp_filho in imports[atual]:
                if imp_filho not in visitados and imp_filho not in stack:
                    stack.append(imp_filho)
                else:
                    return True
    return False


def main():
    i = int(input())

    for _ in range(i):
        num_arquivos, num_import = map(int, input().split())

        imports = {arq: [] for arq in range(1, num_arquivos + 1)}
        for _ in range(num_import):
            arq_um, arq_dois = map(int, input().split())
            imports[arq_um].append(arq_dois)
        
        print(dfs(imports))


if __name__ == '__main__':
    main()