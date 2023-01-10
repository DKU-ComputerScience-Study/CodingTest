def solution(k, tangerine):
    dic = dict()
    
    for x in tangerine :  ## 귤 크기 하나씩 접근
        if x in dic : ## 같은 귤 크기가 있어 
            dic[x] += 1  ## 갯수 +1 
        else : 
            dic[x] = 1 ## 같은 귤크기 없으면 1
    lst = []
    for key ,val in dic.items() : 
        lst.append((val))
    lst.sort(reverse=True)
    
    
    ans = 0 
    cnt = 0
    for i in lst :
        ans += i
        cnt += 1
        if ans >= k : 
            return cnt
        
    
    
