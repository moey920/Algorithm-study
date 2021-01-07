while True:
    T = sorted(list(map(int, input().split())))

    if T[0] == 0: #입력종료
        break
    else:  
        #삼각형 조건변수 설정
        t1 = T[0]**2 + T[1]**2
        t2 = T[2]**2
        
        if T[0] + T[1] < T[2]: #삼각형 불가능 조건 예외처리
            print("error")
        
        elif t1 == t2: # 직삼각형 출력
            print("rightangle")
        
        else : # 삼각형 출력
            print("triangle")