# # 최초 일요일이 1900.1.7
# # 매월 1일의 누적일수가 7로 나누어 떨어지면 일요일

# # 엄밀히 20세기는 1901.01.01년부터 2000.12.31까지이다.
# # 다만 문제에서 1900.01.01부터 나왔으니 1999.12.31일로 계산합니다.

case_a = [31,28,31,30,31,30,31,31,30,31,30,31] # 평년
case_b = [31,29,31,30,31,30,31,31,30,31,30,31] # 윤년
monthlydate,datesum,count = [],0,0

for year in range(1900,2000):
    # 1900~2000년까지 해당 년도가 평년인지 윤년인지 판단
    if year%4 == 0: # 윤년 조건
        if year%100 == 0 and year%400 != 0 : 
            monthlydate = case_a # 400으로 나누어 떨어지지 않으면 평년이다
        else : 
            monthlydate = case_b
    else : # 평년 조건
        monthlydate = case_a

    # 각 월이 가진 날짜 리스트를 date로 받아와서 
    for date in monthlydate: 
        datesum += date
        print(datesum)
        if (datesum-(date-1))%7 == 0: count += 1



import datetime

k = int(input())

s = [0, 0, 0, 0, 0, 0, 0] # 1일이 어떤 요일인지 카운트용 리스트
date = datetime.datetime(1900, 1, 1) # 시작일 초기화
d = datetime.timedelta(days=1) # 하루씩 올라가게 하는 함수
while date.year < 2000 :
    for i in range(k) : 
        if date.day == 1 and date.weekday() == i:
            s[i] += 1
        date += d
        
print(s[i])


s = 0
c = datetime.datetime(1901, 1, 1)
d = datetime.timedelta(days=1)
while c.year < 2001 :
  if c.day == 1 and c.weekday() == 6: #일요일 조건
    s += 1
  c += d
print(s)


# 인선님 코드

# group={0:0, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0}

# year=1900

# month1=[3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]#윤년아님
# month2=[3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]#윤년

# plus_day=1
# result=int(input())

# for i in range(100):
#     if year%4==0 and year%100 !=0:#윤년
#         for j in month2:
#             if j in group.keys():
#                 plus_day += j
#                 group[plus_day%7]+=1
        
        
#     else:#윤년아님
#         for j in month1:
#             if j in group.keys():
#                 plus_day += j
#                 group[plus_day%7]+=1

        
#     year+=year

# print(group[result])