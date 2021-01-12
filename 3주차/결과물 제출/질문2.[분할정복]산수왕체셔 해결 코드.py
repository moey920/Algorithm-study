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




