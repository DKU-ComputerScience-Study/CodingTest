def solution(n):
    three = []
    quo = n
    while True:
        if quo % 3 == 1:
            three.append('1')
        if quo % 3 == 2:
            three.append('2')
        if quo % 3 == 0:
            three.append('4')
            quo -= 1
        quo = (int)(quo / 3)
        if quo == 0:
            break
    three.reverse()
    answer = ""
    for i in three:
        answer += i

    return answer
