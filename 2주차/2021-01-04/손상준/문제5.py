N = int(input())

# 개당 단백질 함량
protein_pure = 250
protein_chicken = 40
protein_peanut = 10

# 총 큐브 개수
total_pure = 0
total_chicken = 0
total_peanut = 0

# 만들 수 없는 경우
error = -1

leftover = N

# 순수 단백질 큐브 개수 추룰 / 남은 단백질 함량
if leftover // protein_pure != 0:
    total_pure = leftover // protein_pure
    leftover = leftover % protein_pure

# 닭 가슴살 큐브 개수 추출  / 남은 담잭질 함량 
if leftover // protein_chicken != 0:
    total_chicken = leftover // protein_chicken
    leftover = leftover % protein_chicken

#  땅콩 큐브 개수 추출 /  남은 담백질 함량
if N // protein_peanut != 0:
    total_peanut = leftover // protein_peanut
    leftover = N % protein_peanut

# 만들 수 없는 경우 판별
if leftover != 0:
    print(error)
else:
    print(total_pure, total_chicken, total_peanut)
