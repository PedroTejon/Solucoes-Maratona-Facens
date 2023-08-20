def dfs(graph, visitados, nodo, objetivo, resultados, count=0):
    if count > 6:
        return False
    elif nodo == objetivo:
        return True

    if nodo not in visitados:
        visitados.add(nodo)
        
        resultados_vizinhos = []
        for vizinho in graph[nodo]:
            resultados_vizinhos.append(dfs(graph, visitados, vizinho, objetivo, resultados, count + 1))
        
        resultados[nodo] = True in resultados_vizinhos
        
    if nodo in resultados:
        return resultados[nodo]
    else:
        return False


def main():
    i = int(input())

    for _ in range(i):
        num_pessoas, num_op = map(int, input().split())

        graph = {p: [] for p in range(1, num_pessoas + 1)}

        for _ in range(num_op):
            op, p1, p2 = map(int, input().split())

            if op == 1:
                graph[p1].append(p2)
                graph[p2].append(p1)
            else:
                print('S' if dfs(graph, set(), p1, p2, {}) else 'N')


if __name__ == '__main__':
    main()