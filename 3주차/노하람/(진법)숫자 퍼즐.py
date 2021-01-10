
K = int(input())
K = format(K, 'b')
# print(K)
result = ''
for i in range(len(K)) :
    if K[i] == '1' :
        result += '4'
    else :
        result += '7'
print(result)