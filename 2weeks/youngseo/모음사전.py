alpha = ['A','E','I','O','U']
global cnt
cnt = -1
def recur(string,ori, dep) :
    if dep >= 6 : 
        return 0
    global cnt
    cnt += 1 
    if string == ori : 
        return 1
    for a in alpha : 
        if(recur(string+a,ori, dep+1)) :
            return 1 

def solution(word):
    recur("",word, 0)
    return cnt
