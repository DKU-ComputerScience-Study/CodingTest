def solution(k, tangerine):
    answer = 0
    temp = [0 for i in range(max(tangerine))]
    for i in tangerine:
        temp[i-1] += 1
    temp.sort(reverse=True)
    for i in range(max(tangerine)):
        k -= temp[i]
        answer += 1
        if (k <= 0):
            break
    return answer
