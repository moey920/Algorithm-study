def is_rightangle(a, b, c):
    return True if a**2 + b**2 == c**2 else False

def main():
    while True:
        triangle = sorted(list(map(int, input().split())))

        if 0 in triangle:
            break

        if is_rightangle(*triangle):
            print("rightangle")
        else:
            print("triangle")

if __name__ == '__main__':
    main()
