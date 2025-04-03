## 1. 재귀(Recursion)

> [!note] 재귀란?
> **자기 자신을 호출하는 함수**를 사용하여 문제를 해결하는 기법
-> 주어진 문제를 **더 작은 하위 문제로 나누어** 반복적으로 해결하는 방식

```java
int sum(int x){
	if (x <= 0) return 0;
	return x + sum(x-1);
}
```

### 1-1. 재귀 사용은 언제 사용해야 할까?
1) 문제를 비슷한 구조의 더 작은 문제로 나눌 수 있는 경우
2) 반복문이 많이 중첩되거나 중첩 횟수가 고정되지 않은 경우
3) 계속 변화하는 변수 사용을 줄여 프로그램 오류 발생 가능성을 줄이고 싶은 경우

> [!danger] 주의
> 재귀를 활용한다고 무조건 효율적인 것은 아님!
> 상황에 맞게 사용해야 한다.

### 1-2. Stack Overflow
1) 무한 재귀
2) 혹은 매우 큰 수
3) 혹은 종결문이 절대 참이 될 수 없는 경우

이런 경우에 스택 오버플로우가 발생할 수 있기에 재귀는 신중하게 사용해야 한다.

### 1-3. 재귀 작성법(fibonacci)
```java
public int fibonacci(int num){
	if(num < 2)
	    return num;
    return fibonacci(num-2) + fibonacci(num-1);
```

num = 4 인 경우,
fibonacci(4) -> fibonacci(2)+fibonacci(3) 
fibonacci(3) -> fibonacci(1)+fibonacci(2) 
fibonacci(2) -> fibonacci(0)+fibonacci(1) 

fibonacci(0) -> num < 2 TRUE -> return 0;
fibonacci(1) -> num < 2 TRUE -> return 1;

fibonacci(2) -> 0 + 1 = 1
fibonacci(3) -> 1 + 1 = 2
fibonacci(4) -> 1 + 2 = 3

fibonacci(4)는 종료되면서 결과값 3을 반환한다.

## 2. 백트래킹(Backtracking)

> [!note] 백트래킹이란?
> 해를 찾는 도중 해가 아니라면 되돌아가서 다시 해를 찾아가는 기법
> 완전탐색을 하는 과정에서 조건에 맞지 않는 부분을 가지치기함

**모든 가능한 경우의 수 중에서 특정한 조건을 만족하는 경우만 살펴보는 것이다!** 
즉, 답이 될만한 가능성이 없으면 더 이상 탐색을 진행하지 않고 
가지치기를 하면서 최적해를 구하는 것.

### 2-1. vs 완전 탐색

> [!note] 완전 탐색이란?
> 모든 경우를 탐색해가면서 무언가를 세거나 어떤 조건이 가능한 경우가 있는 확인하는 방법
> ex) DFS, BFS

#### 언제 사용하는가
- 발생 가능한 경우의 수가 충분히 적은 경우
- 따져야 하는 **상황이 특정 규칙에 따라 발생하지 않는** 경우
- 각각의 경우에 **따져야 하는 상황이 명확한** 경우

### 2-2. 백트래킹은 언제 사용해야 할까?

1) 완전 탐색 조건은 기본적으로 만족할 때
2) 초기 상태에서 목표 상태에 도달하기 위해 상태를 전이시키면서 나아갈 수 있는 경우
3) **탐색 중간 시점에서** 특정 경우가 **조건에 부합하는 지 판단 가능한** 경우

### 2-3. 백트래킹 작성법
아래와 같이 각 조건에 따라 재귀 형식으로 호출하도록 작성하는 예시가 많다.

```js
function backtrack(idx, currentValue, plus, minus, multi, divide) {

	if (idx === n) {
		maxResult = Math.max(maxResult, currentValue);
		minResult = Math.min(minResult, currentValue);
		return;
	}

	if (plus > 0) {
		backtrack( idx + 1, currentValue + numbers[idx], plus - 1, minus, multi,divide);
	}
	...
}
```