def power(x, y):
    if y == 0:
        return 1


    semi_result = power(x, y // 2)
    
   
    if y % 2 == 0:
        return semi_result * semi_result
    else:
        return x * semi_result * semi_result


A, B, C=map(int, input().split())





print(power(A, B)%C)
