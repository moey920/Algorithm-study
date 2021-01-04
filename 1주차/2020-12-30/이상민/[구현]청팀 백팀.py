"""
[구현]청팀 백팀

공백으로 구분되게 입력된 점수를 list로 형변환하고, 합을 구하여 저장.
두 팀의 총 점수를 비교하여 점수가 더 높은 팀의 점수를 출력
"""

blue_score = sum(list(map(int, input().split())))
white_score = sum(list(map(int, input().split())))

if blue_score >= white_score:
    print(blue_score)

elif blue_score < white_score:
    print(white_score)