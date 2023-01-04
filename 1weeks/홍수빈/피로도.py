def solution(k, dungeons):
    answer = 0
    m = len(dungeons)
    arr = [0 for i in range(m)]
    isused = [0 for i in range(m)]
    perm = []

    def backtracking(k):
        temp = []
        if k == m:
            for i in range(m):
                temp.append(arr[i])
            perm.append(temp)
            return
        for i in range(m):
            if isused[i] == 0:
                isused[i] = 1
                arr[k] = i
                backtracking(k+1)
                isused[i] = 0

    backtracking(0)
    permlen = len(perm)
    life = k
    for i in range(permlen):
        k = life
        maxi = 0
        for j in perm[i]:
            if (dungeons[j][0] <= k):
                k -= dungeons[j][1]
                maxi += 1
        if answer < maxi:
            answer = maxi
    return answer
