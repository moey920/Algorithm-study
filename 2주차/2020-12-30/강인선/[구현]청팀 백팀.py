w1, w2, w3, w4=map(int, input().split())

b1, b2, b3, b4=map(int, input().split())

sum_w=w1+w2+w3+w4

sum_b=b1+b2+b3+b4

if sum_w>sum_b:
    print(sum_w)
else:
    print(sum_b)