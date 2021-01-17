def main(n) :
    result = 0
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    if n == 3 :
        return 3
    else :
        result = (n-1) * main(n-1) # 내가 선택할 수 있는 무기의 수 : n-1개, 전체 경우의 수 : 내가 선택가능한 무기 수 * n-1명일 때 경우의 수(main(n))
        return result

    
if __name__ == "__main__" :
    n = int(input())
    print(main(n))