## [입력]
- 자연수 N과 K를 입력합니다.
```math
(1<=N<=1,000,000,000)
(1<=K<=50)
```

## [출력]

- $` 1^K + 2^K + … + + N^K`$  
 를 1,000,000,009로 나눈 나머지를 출력합니다.
 
## [풀이]

- N의 범위가 `10억`까지이기 때문에, 거듭제곱 연산의 효율성을 아무리 고친다 해도, `N번 반복`하면 무조건   
  시간 초과가 날 수밖에 없다.
- 따라서 `N번 반복을 하지 않는 방법`을 찾아내야 한다.
- `거듭제곱의 합` 공식을 찾아본 결과, **베르누이 공식** 이라는 것을 찾아냈다.
- 구현하기에 너무 어려운 개념이고, 쉬움 난이도의 문제와 적합하지 않다고 생각하여 포기했다...

- 아래 코드는 정답 코드를 가져온 것인데, 나름의 해석을 해보았다.

    - 베르누이 수를 DP로 구하기 위하여 `MAX_K` 까지의 pascal 삼각형을 만든다
    - 주어진 `MAX_K`까지의 베르누이 수를 구한다.
    - n과 K를 입력받고, `베르누이 공식`을 적용하여 거듭제곱의 합을 구한다. (X)
        - (출력해보니 x에 모듈러 역수를 곱해야 거듭제곱의 합이 된다.)
    - 모듈러 연산 시 연산속도 향상을 위해 `유클리드 알고리즘`을 이용한 `egcd` 함수 선언
    - K + 1의 모듈러 역수(modular inverse)를 구하여, x와 곱하여 답을 구한다.
    
- 정말 너무 어려운 것 같다.. 풀이가 이게 아닌 것 같으니 질문해야 함.

```python
MAX_K = 50
MOD = 1000000009


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a):
    g, x, y = egcd(a, MOD)
    return x % MOD


if __name__ == '__main__':

    # Generate Pascal's triangle
    pascal = [[1]]

    while len(pascal) <= MAX_K + 1:
        n = len(pascal)
        pascal.append(list(map(sum, zip([0] + pascal[-1], pascal[-1] + [0]))))

    # Generate Bernouli numbers
    bernoulli = [1]

    while len(bernoulli) <= MAX_K:
        n = len(bernoulli)

        if n == 1:
            bernoulli.append(-modinv(n + 1) % MOD)
        elif n % 2 == 1:
            bernoulli.append(0)
        else:
            x = pascal[n + 1][1] * bernoulli[1]
            x += sum(pascal[n + 1][i] * bernoulli[i] for i in range(0, n, 2))
            bernoulli.append(-x * modinv(n + 1) % MOD)

    n, K = map(int, input().split())

    x = sum(pow(-1, i) * pascal[K + 1][i] * bernoulli[i] * pow(n, K + 1 - i, MOD) for i in range(K + 1))
    print(x * modinv(K + 1) % MOD)
    print(x)
    print(modinv(K + 1))
```