def dijkstra(graph, src, dest):
    distance = {node: 0 for node in graph.keys()}
    distance[src] = 1
    
    visitados = set()
    while True:
        atual = max(distance, key=lambda x: distance[x])
        if atual == dest:
            break
        
        for nodo, distancia in graph[atual]:
            if nodo not in visitados and distance[nodo] < distance[atual] * (1 - distancia):
                distance[nodo] = distance[atual] * (1 - distancia)

        del distance[atual]
        visitados.add(atual)

    return distance[dest]


def main():
    i = int(input())
    for _ in range(i):
        numero_cidades, numero_estradas = map(int, input().split())
        graph = {}
        for x in range(1, numero_cidades + 1):
            graph[x] = []

        for x in range(numero_estradas):
            cidade_um, cidade_dois, perda = input().split()
            cidade_um = int(cidade_um)
            cidade_dois = int(cidade_dois)
            perda = float(perda)

            graph[cidade_um].append((cidade_dois, perda))
            graph[cidade_dois].append((cidade_um, perda))

        menor_perda = dijkstra(graph, 1, numero_cidades)
        print(f'{(1 - menor_perda) * 100:.2f}%')


if __name__ == '__main__':
    main()