import copy
def drop(n, m, answer1):
    for j in range(0, n):
        for i in range(m-1, 0, -1):
            if answer1[i][j] == 0:
                answer1[i][j] = answer1[i-1][j]
                answer1[i-1][j] = 0
    return answer1
    
def test(n, m, drop_Answer):
    answer2 = copy.deepcopy(drop_Answer)
    final_answer = findsame(n, m, answer2)
    i = 0
    while i < m:
        final_answer = findsame(n, m, final_answer)
        i += 1
    for j in range(0, m):
        for k in range(0, n):
            print(final_answer[j][k], end=' ')
        print("", end='\n')

def findsame(n, m, answer2):
    answer1 = copy.deepcopy(answer2)
    for i in range(0, m):
        for j in range(0, n):
            if j+1 < n:    #是否超出字串最右邊
                if answer2[i][j] == answer2[i][j+1]:
                    answer1[i][j] = 0
                    answer1[i][j+1] = 0
    for k in range(0, n):
        for l in range(0, m):
            if l+1 < m:
                if answer2[l][k] == answer2[l+1][k]:
                    answer1[l][k] = 0
                    answer1[l+1][k] = 0
    final_answer1 = drop(n, m, answer1)
    return final_answer1

def main():
    n,m = map(int, input("請輸入字串長度以及多少字串:").split()) #n代表字串長度 m代表多少字串
    line = [[0]*n]*m       
    for i in range(m):
        line[i] = input().split(" ")
        if len(line[i]) != n:
            print("輸入字串長度不符")
            exit()
    answer = copy.deepcopy(line)
    test(n, m, answer)

main()