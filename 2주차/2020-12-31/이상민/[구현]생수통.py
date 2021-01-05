"""
[구현]생수통

3개의 입력값 중 최소값 + 2개의 입력값 중 최소값 + 10
"""

bottle = min([int(input()) for _ in range(3)])
head = min([int(input()) for _ in range(2)])

print(bottle + head + 10)