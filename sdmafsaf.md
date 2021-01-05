## 풀이방법

- 청팀과 백팀의 스코어를 입력받고, 합을 저장한다
- 각 조건에 맞게 결과를 출력한다.


### 코드
```python
blue_score = sum(list(map(int, input().split())))
white_score = sum(list(map(int, input().split())))

if blue_score >= white_score:
    print(blue_score)

elif blue_score < white_score:
    print(white_score)
```
