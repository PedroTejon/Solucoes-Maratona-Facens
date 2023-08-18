def main():
    i = int(input())

    for _ in range(i):
        n = int(input())

        nums = list(map(int, input().split()))
        if n == 1:
            print(0)
            continue
        
        nums_unicos = set(nums)

        size = 0
        for num in nums_unicos:
            contagem = nums.count(num)
            if (n % 2 == 0 and contagem % 2 == 0) or contagem == 1:
                size += 1            

        print(size)


if __name__ == '__main__':
    main()