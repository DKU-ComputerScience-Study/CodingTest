## dfs + 백트래킹 ??..

chk = [0] * 9 ## 방문 배열

def dfs(n, rk, dungeons) :
    
    ans = n 
    for i in range(len(dungeons)) :  ## 처음부터 끝까지 탐색
        if chk[i] : ##이미 갔으면 넘어간다.
            continue
        
        if (rk >= dungeons[i][0]) and (rk >=dungeons[i][1]): ## 피로도 조건 
            chk[i] = 1
            ans = max(dfs(n+1, rk-dungeons[i][1], dungeons), ans) ## 다음 dfs함수로
            chk[i] = 0 ## 다시 안갔다 표시
    return ans ## 값 반환
def solution(k, dungeons):
    answer = dfs(0, k, dungeons) ## 몇번째 던전인지, 남은 피로도, 던전 배열
    
    return answer 
