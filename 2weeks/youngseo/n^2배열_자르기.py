def solution(n, left, right):
    answer = []
    
    for i in range(left+1, right+2) :
        l = i//n+1 if i%n else i//n
        r = i%n if i%n else n
        # print(i, l,r)
        answer.append(max(l,r))
        
    return answer
    

