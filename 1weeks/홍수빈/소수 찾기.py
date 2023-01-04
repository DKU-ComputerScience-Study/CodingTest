def solution(numbers):
    numarr = []  # numbers 문자열을 나누어 문자를 담을 리스트
    for i in numbers:
        numarr.append(i)
    numarrlen = len(numarr)  # numarr의 길이(문자의 개수)

    arr = [0 for i in range(numarrlen)]
    # 백 트래킹에서 각 문자가 담길 리스트
    isused = [0 for i in range(numarrlen)]
    # 백 트래킹에서 각 문자 체크 여부(0,1)를 확인하는 리스트

    primechecklist = []
    # ex) "17" => [1,7,17,71] / "011" => [0, 1, 10, 11, 101, 110]

    def backtracking(numarr, m, k):
        # numarr은 문자열을 나누어 담은 리스트
        # m은 numarr로 만들 문자의 자릿 수 ex) "011", m=2 => [10,11]
        # k는 재귀를 관리하기 위한 변수, 0부터 시작
        arrstring = ""
        if k == m:
            for i in range(m):  # 구할 자릿 수(m) 만큼 반복
                arrstring += arr[i]
            num = int(arrstring)
            for i in primechecklist:
                if i == num:
                    return
            primechecklist.append(num)
            return

        for i in range(len(numarr)):  # [1,7] => 2 / [0,1,1] => 3
            if isused[i] == 0:  # isused는 전부 0으로 초기화 되어있음
                arr[k] = numarr[i]  # 첫 시도, arr[0]에 numarr[0]을 대입
                isused[i] = 1  # isused[0] = 1
                backtracking(numarr, m, k+1)  # 재귀 함수 사용해서 k를 1 높임
                isused[i] = 0

    for i in range(1, numarrlen+1):
        backtracking(numarr, i, 0)
    # print(primechecklist)

    # 소수 판별 알고리즘(추후 에라토스테네스의 체 외울 것)
    primecount = 0
    isprime = 0
    import math
    for i in primechecklist:
        isprime = 1
        if i == 1 or i == 0:
            continue
        for k in range(2, int(math.sqrt(i))+1):
            if i % k == 0:
                isprime = 0
        if isprime == 1:
            primecount += 1
    answer = primecount
    return answer
