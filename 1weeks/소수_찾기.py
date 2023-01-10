A = set()
chk = [0]*8
prime = [1] * 10000001
prime[0] = 0 
prime[1] = 0
def func(cnt, curr,numbers) :
    if cnt == len(numbers) : 
        return
    
    for s in range(len(numbers)) :
        if chk[s] : 
            continue
        if prime[int(curr+numbers[s])] :
            A.add(int(curr+numbers[s]))
        chk[s] = 1
        func(cnt+1, curr+numbers[s], numbers)
        chk[s] = 0
    

def solution(numbers):
    for i in range(2, 33333) :
        if not prime[i] :
            continue
        for j in range(i+i, 10000000, i) :
            prime[j] = 0
            
    func(0, "", numbers)
    
    return len(A)
    
