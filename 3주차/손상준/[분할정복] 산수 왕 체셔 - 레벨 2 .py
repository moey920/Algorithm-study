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