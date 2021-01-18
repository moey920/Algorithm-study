from collections import deque
import sys 

if __name__ == "__main__" :
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    answer = sys.maxsize
    left, right = 0, 0 # 포인터 변수들
    cnt = 0
    q = deque()

    for start in range(n) :

        while right < n and cnt < k : # 끝 값이 주어진 병정 수 인덱스보다 작고, 카운트가 K명 이하인 경우 반복
            q.append(a[right]) # 1이건, 2건 큐에 삽입하고
            if a[right] == 1 : # 지금 삽입된 숫자가 1이면(다이아몬드 병정이면)
                cnt += 1 # 카운트를 하나 올린다
            right += 1 # right 포인터 이동
            
        if cnt == k : # 집합 안에 1이 K개 들어있는 경우
            answer = min(len(q), answer) #지금까지 있었던 ans들과, 현재 큐의 길이(len(q)) 중 최소값을 ans로 설정한다
            if a[left] == 1 : # left 포인터의 위치에 1이 들어있으면(다이아몬드 병정이면)
                cnt -= 1 # left가 1 이동하면 집합 내에 1이 하나 사라지니까 cut를 하나 줄인다
            left += 1 # left 포인터 이동
            q.popleft() # left가 하나 이동했으니, 큐에 들어있던 가장 좌측 요소를 pop한다.

    print(answer if answer != sys.maxsize else -1)
    # if answer != sys.maxsize :
    #     print(answer)
    # else :
    #     print(-1)