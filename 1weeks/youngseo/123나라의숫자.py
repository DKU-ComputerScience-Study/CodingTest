## 삼진법
## 0 1 2
## 1 2 4

def solution(n):
    answer = ''
    
    while n>3 :
        if n%3 : ## 3으로 안나뉘어떨어지면
            answer += str(n%3)
            n //= 3
        else : ## 3으로 나누어 떨어지면
            answer += "4"
            n = n//3-1
    
    if n<=2 : 
        answer += str(n)
    else : 
        answer += "4"
        
    answer = answer[::-1]
    return answer






