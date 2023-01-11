def solution(word):
    # 5**5
    alpha = ['A', 'E', 'I', 'O', 'U']
    dic = []
    arr = [0 for i in range(5)]

    def dfs(k, m):
        tempstr = ""
        if k == m:
            for i in range(m):
                tempstr += arr[i]
            dic.append(tempstr)
            return
        for i in alpha:
            arr[k] = i
            dfs(k+1, m)
    for i in range(1, 6):
        dfs(0, i)
    dic.sort()
    print(dic.index(word) + 1)
    answer = dic.index(word) + 1
    return answer
# A / AA / AAA / AAAA /
# AAAAA / AAAAE / AAAAI / AAAAO / AAAAU
# AAAE / AAAI / AAAO / AAAU
# AAE / AAI / AAO / AAU
# AE / AI / AO / AU
