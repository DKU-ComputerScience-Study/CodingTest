import sys
sys.setrecursionlimit(1000000)

DP = [0] * 100_001

def fibo(n):
    if n <= 2 :
        return 1
    
    if DP[n] :
        return DP[n]
    DP[n] = (solution(n-1)+solution(n-2))%1234567
    
    return DP[n]


def solution(n):
    return fibo(n)

