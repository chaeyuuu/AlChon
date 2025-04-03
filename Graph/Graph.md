# 그래프
**G (V, E)**
- 그래프는 정점의 집합 V와 간선의 집합 E로 이루어져 있다.
- 하나의 정점에는 여러 정점이 이어질 수 있다.
- 대표적인 비선형 자료구조(한 개의 원소 뒤에 여러 개의 원소가 존재)

**그래프의 종류**
- 단방향 그래프
- 양방향 그래프
- 가중치 그래프
- 연결 그래프: 모든 정점끼리 간선을 통해 이동할 수 있는 그래프
- 트리: 사이클이 존재하지 않는 연결 그래프
- DAG: 사이클이 존재하지 않는 방향 그래프
- 포레스트: 트리의 집합
- 이분 그래프: 정점을 두 그룹으로 나눌 수 있는 그래프, 각 그룹은 다른 그룹으로만 간선을 이을 수 있다.
- 완전 그래프: 서로 다른 두 정점을 잇는 간선이 모두 존재하는 그래프

**그래프를 나타내는 방법**
1. 인접 행렬
  - 그래프를 𝑁 × 𝑁 행렬 𝐴로 나타내고, 𝐴𝑖,𝑗 가 1인 경우 𝑖 → 𝑗 를 잇는 간선이 있다는 의미
  - 정점이 많아질수록 공간 낭비가 심함 -> 𝑂(|𝑉|^2) 의 공간 사용
2. 인접 리스트
  - 노드를 나타내는 리스트에 연결된 다른 노드들을 저장 (ex. list 0번째 index에 2, 4, 5 저장)
  - 각 리스트를 가변 리스트로 구현해 메모리 낭비를 최소화 -> 𝑂( |𝑉| + |𝐸| ) 의 공간 사용
<img width="498" alt="스크린샷 2025-04-02 02 05 15" src="https://github.com/user-attachments/assets/b5eb32aa-c412-429e-b352-a876d9b5effd" />

---

**그래프 순회**
- 노드를 특정 순서로 방문하는 방법을 의미

   ```

      A
     / \
    B   C
   / \
  D   E

   ```

1. 전위 순회
    - 순서: 현재 노드 → 왼쪽 서브트리 → 오른쪽 서브트리
    - 전위 순회 결과: A, B, D, E, C

2. 중위 순회
    - 순서: 왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리
    - 중위 순회 결과: D, B, E, A, C

3. 후위 순회
    - 순서: 왼쪽 서브트리 → 오른쪽 서브트리 → 현재 노드
    - 후위 순회 결과: D, E, B, C, A

---

**그래프 탐색**
1. 깊이 우선 탐색 (DFS)
    -  가능한 한 깊게 탐색을 진행한 후, 더 이상 진행할 수 없게 되면 백트래킹하여 다른 경로를 탐색하는 방식
   1. 임의의 정점에서 시작해서, 인접한 정점 중 방문하지 않은 정점을 방문
   2. 방문한 정점에서 다시 탐색
   3. 모든 인접한 정점이 이미 방문되었다면, 이전 정점으로 돌아가기
   - 재귀호출 또는 stack 활용
   ```
   def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # 방문 노드 출력

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

    def dfs_stack(graph, start):
        visited = set()  # 방문한 노드를 저장할 집합
        stack = [start]  # 시작 노드를 스택에 추가

        while stack:
            node = stack.pop()  # 스택에서 노드 추출
            if node not in visited:
                visited.add(node)  # 노드 방문 처리
                print(node)  # 방문 노드 출력

                # 연결된 노드를 스택에 추가 (역순으로 추가하여 올바른 순서로 처리)
                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    # 그래프 예시 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    dfs(graph, 'A')

   ```

    
2. 너비 우선 탐색 (BFS)
    - 시작 노드에서 가까운 노드부터 차례로 탐색하며, 각 노드를 탐색한 후 그 노드와 연결된 노드를 큐에 추가하여 탐색
    1. 임의의 정점에서 시작해서, 인접한 정점 중 방문하지 않은 모든 정점들을 방문
    2. 이후에 방문할 정점들은 앞에서 방문해야하는 정점들을 모두 방문한 후 처리
    - 현재 정점과 인접한 정점 중 방문하지 않은 모든 정점을 다음번 방문해야한다.
    - 큐를 사용해서 구현

    ```
    from collections import deque

    def bfs(graph, start):
        visited = set()
        queue = deque([start])  # 큐 초기화
        visited.add(start)

        while queue:
            node = queue.popleft()  # 큐에서 노드 추출
            print(node)  # 방문 노드 출력

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)   # 큐에 추가할때 방문 체크
                    queue.append(neighbor)  # 큐에 추가

    # 그래프 예시 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs(graph, 'A')

    ```
    - 큐에 넣을때 방문 체크해야한다.
    - 사이클이 존재하는 그래프의 경우, 정점에 방문할 때 체크하면 문제 발생
    - 큐에 하나의 정점이 여러개 들어가게 된다. -> 메모리 초과 가능성
