N = list(map(int, input().split()))
T = list(map(int, input().split()))


total_work = N[0] #총 주문 개수

capable_time = N[1] #근무가능 시간

sum_work = 0 #근무 시간
capable_work = 0 #주문 가능 개수


for i in range(total_work):

    sum_work = sum_work + T[i]

    if sum_work <= capable_time: #근무가능 시간 /근무시간 비교
        capable_work = i + 1
    else: #근무시간 초과
        if i == 0:
            capable_work = 0
        else:
            break

print(capable_work)
