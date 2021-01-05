b1, b2, b3, b4 = map(int, input().split())

w1, w2, w3, w4 = map(int, input().split())

b_sum = b1 + b2 + b3 + b4
w_sum = w1 + w2 + w3 + w4

if b_sum >= w_sum:
    print(b_sum)
else:
    b_sum < w_sum
    print(w_sum)