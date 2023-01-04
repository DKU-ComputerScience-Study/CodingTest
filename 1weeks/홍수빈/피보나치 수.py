def solution(k):
    f = [0 for i in range(k+1)]
    f[0] = 1
    f[1] = 1
    for i in range(2, k+1):
        f[i] = (f[i-1] + f[i-2]) % 1234567
        # 중간결과를 배열에 저장하면서 진행(DP)
    return f[k-1]
