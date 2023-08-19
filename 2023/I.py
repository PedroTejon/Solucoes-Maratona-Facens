def dfs(visitados, graph, node, recStack):
    if node not in visitados:
        visitados.add(node)
        recStack.add(node)
        neighbour_results = []
        for neighbour in graph[node]:
            neighbour_results.append(dfs(visitados, graph, neighbour, recStack)) 
            
        if any(neighbour_results):
            return True
        else:
            recStack.remove(node)
            return False
    elif node in recStack:
        return True
    else:
        return False


def main():
    i = int(input())

    for _ in range(i):
        num_arquivos, num_import = map(int, input().split())

        imports = {arq: [] for arq in range(1, num_arquivos + 1)}
        for _ in range(num_import):
            arq_um, arq_dois = map(int, input().split())
            imports[arq_um].append(arq_dois)
        
        print("Imports with cycles are not allowed" if dfs(set(), imports, 1, set()) else "Good to go")


if __name__ == '__main__':
    main()