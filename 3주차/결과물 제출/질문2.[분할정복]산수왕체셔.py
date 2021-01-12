##질문

1. 시간 초과 문제가 해결되지 않음.
2. 시간 초과 문제 왜 발생하는지?
3. 아래의 ##2., ##3. 풀이가 비슷하나, 3번은 시간초과문제가 해결되지 않음. 그러한 차이가 생기는 이유?

4. 분할정복 문제 유형의 문제풀이 접근 방법.




## 문제 풀이 코드

##1.

a, b, c = map(int, input().split())
ans = (a**b) % c
print(ans)


##2.

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우

if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)


##3.

def power(x, y):
    if y == 0:
        return 1


    semi_result = power(x, y // 2)
    
   
    if y % 2 == 0:
        return semi_result * semi_result
    else:
        return x * semi_result * semi_result


A, B, C=map(int, input().split())


##4.

def Recursive_Power(C,n):
    if n ==1:
        return C
    if n % 2==0:
        y = Recursive_Power(C,n/2)
        return y*y
    else:
        y= Recursive_Power(C,(n-1)/2)
        return y*y*C
        
A, B, C = map(int, input().split())

K = Recursive_Power(A, B) % C
print(K)




