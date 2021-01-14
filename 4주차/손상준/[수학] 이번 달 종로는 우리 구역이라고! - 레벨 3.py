day = [i for i in range(8)]
cnt_firstday = {day == 0 for day in day}

month1=[3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
month2=[3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3] # 윤년일 경우

day_index=1
result=int(input())

for i in range(100):
    if i%4==0 and i%100 !=0: # 윤년일 경우
        for j in month2:
            if j in day.keys():
                day_index += j
                day[7]+=1
    else:
        for j in month1:
            if j in day.keys():
                day_index += j
                day[day_index%7]+=1

