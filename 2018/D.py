def main():
    i = int(input())

    for _ in range(i):
        qntd_num, qntd_oper = map(int, input().split())

        nums = [0] * qntd_num

        for _ in range(qntd_oper):
            inps = list(map(int, input().split()))
            
            if inps[0] == 0:
                oper, index_i, index_f, valor = inps
            else:
                oper, index_i, index_f = inps
            
            if oper == 0:
                for i in range(index_i, index_f + 1):
                    nums[i] += valor
            elif oper == 1:
                print(sum(nums[index_i: index_f + 1]))



if __name__ == '__main__':
    main()