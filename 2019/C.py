n = int(input())

for _ in range(n):
    larg, qntd = map(int, input().split())

    soma = 0
    cadeia = input()
    for i in range(qntd):
        Li, Ri = map(int, input().split())

        
        char_count = {}
        for char in cadeia[Li - 1: Ri]:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        if len(list(filter(lambda x: x % 2 == 1, char_count.values()))) <= 1:
            soma += 1
    
    print(soma)