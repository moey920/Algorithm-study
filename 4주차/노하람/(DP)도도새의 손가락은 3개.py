import sys # 파이썬은 무한 재귀함수 호출을 제한하기 위해서 1000번 제한이 default이다. 이를 바꿔주기 위한 모듈

def main(n) :
    # n이 1,2,3 일 땐 규칙을 사용할 수 없으므로 예외 처리하는 구문
    if n == 1 : # {1}
        return 1
    if n == 2 : # {1+1, 2}
        return 2
    if n == 3 : # {1+1+1, 1+2, 2+1, 3}
        return 4
    # 재귀함수를 이용
    else :
        return main(n-1)%123456 + main(n-2)%123456 + main(n-3)%123456
        # or
        # return (main(n-1) + main(n-2) + main(n-3))%123456

if __name__ == "__main__" :
    sys.setrecursionlimit(10000) # 재귀함수 호출 제한을 늘려보았지만 시간초과나, 호출 제한(5번 테스트케이스)은 해결하지 못함.
    n = int(input())
    print(main(n))
