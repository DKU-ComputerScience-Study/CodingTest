def solution(n, left, right):
    # 첫번째 시도 3중배열
   # tdarr = [[0 for col in range(n)] for row in range(n)]
    # for i in range(1,n+1):
    #   for col in range(i):
    #      for row in range(i):
    #         if(tdarr[col][row] == 0):
    #            tdarr[col][row] = i
    # 0,0
    # 0,0 / 0,1 / 1,1 / 1,0
    # 0,2/ 1,2 / 2,2 / 2,0 / 2,1
    # print(tdarr)

    # 두번째 시도 2중배열
    #     for col in range(1,n+1):
 #       for row in range(1,n+1):
  #          if col > row:
   #             answer.append(col)
    #        elif row > col:
    #           answer.append(row)
    #      else:
    #         answer.append(col)

    # 3번째 시도 규칙 찾아 구현
    answer = []
    # y는 n보다 높아질 수가 없음
    # x, y에다 left의 몫, 나머지를 넣어서 거기서부터 체크해야함
    x = (int)(left / n) + 1
    y = left % n  # 0,1,2,3
    for i in range(left, right+1):
        y += 1
        if x > y:
            answer.append(x)
        elif x < y:
            answer.append(y)
        else:
            answer.append(x)
        # print("({},{})".format(x,y))
        if y == n:
            x += 1
            y = 0
    # n = 3
    # 123456789 (index+1)
    # 123223333 ()value)
    # 123123123 (i % 3)
    # 001112223 (i / 3)
    # 1. 1,1(1) / 2. 1,2(2) / 3. 1,3(3)
    # 4. 2,1(2) / 5. 2,2(2) / 6. 2,3(3)
    # 7. 3,1(3) / 8. 3,2(3) / 9. 3,3(3)

    return answer
