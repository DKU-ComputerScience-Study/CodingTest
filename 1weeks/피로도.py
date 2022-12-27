import itertools


def solution(k, dungeons):
    answer = 0
    dunlen = len(dungeons)
    temp = [i for i in range(dunlen)]
    # 던전 길이만큼 리스트 생성(던전은 0부터 시작해서 최대길이까지 존재)
    # 반복문이 모든 경우의 수를 탐색하도록 해야함
    # 만약 길이가 3이면
    # => 0,1,2 / 0,2,1 / 1,0,2 / 1,2,0 / 2,0,1 / 2,1,0
    # 근데 이러면 시간초과 할 것 같아
    # 되네
    perm = list(itertools.permutations(temp, dunlen))
    # 순열사용
    permlen = len(perm)  # 모든 경우의 수의 개수
    temp = k  # 순열로 나온 리스트들마다 k를 초기화 시키기 위한 임시 변수

    for i in range(permlen):  # 던전을 도는 경우의 수만큼 반복
        k = temp
        maxi = 0  # 최대 던전 탐색 횟수
        for j in perm[i]:
            if (dungeons[j][0] <= k):
                k -= dungeons[j][1]
                maxi += 1
        if answer < maxi:
            answer = maxi
    return answer
