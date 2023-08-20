def djikstra(graph, start, end):
    distances = {nodo: float('inf') for nodo in graph}
    distances[start] = 0

    visitados = set()
    while True:
        atual = min(distances, key=lambda x: distances[x])
        if atual == end:
            break

        for nodo, distancia in graph[atual]:
            if nodo not in visitados and distances[nodo] > distances[atual] + distancia:
                distances[nodo] = distances[atual] + distancia
    
        del distances[atual]
        visitados.add(atual)
    
    return distances[end] if distances[end] != float('inf') else 'CAMINHO INEXISTENTE'
    

def main():
    while True:
        qntd_linha, *pontos = map(int, input().split())
        if qntd_linha == 0:
            break

        graph = {n: [] for n in range(qntd_linha)}
        for i in range(qntd_linha):
            for j in range(qntd_linha):
                velocidade = pontos[i * qntd_linha + j]
                if velocidade != 0:
                    graph[i].append([j, velocidade])
              
        print(djikstra(graph, 0, qntd_linha - 1))


if __name__ == '__main__':
    main()