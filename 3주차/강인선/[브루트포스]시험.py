N=int(input())

ans=input()


blue='54321'*20
red='12345'*20
yellow='3'*100

ans_blue=blue[0:N]
ans_red=red[0:N]
ans_yellow=yellow[0:N]

correct_blue=0
correct_red=0
correct_yellow=0

for i in range(N):
    if ans_blue[i]==ans[i]:
        correct_blue+=1
    if ans_red[i]==ans[i]:
        correct_red+=1    
    if ans_yellow[i]==ans[i]:
        correct_yellow+=1
        
print(max(correct_blue, correct_red, correct_yellow))

if correct_blue==correct_red:
    if correct_yellow==correct_red:
        print('red')
        print('blue')
        print('yellow')
        
    else:
        print('red')
        print('blue')
    
elif correct_blue==correct_yellow:

    if correct_yellow==correct_red:
        print('red')
        print('blue')
        print('yellow')
    else:
        print('blue')
        print('yellow')    


elif correct_yellow==correct_red:

    if correct_yellow==correct_blue:
        print('red')
        print('blue')
        print('yellow')
    else:
        print('red')
        print('yellow')

elif max(correct_blue, correct_red, correct_yellow)==correct_blue:
    print('blue')
elif max(correct_blue, correct_red, correct_yellow)==correct_red:
    print('red')
elif max(correct_blue, correct_red, correct_yellow)==correct_yellow:
    print('yellow')