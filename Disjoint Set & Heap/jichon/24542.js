const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

//disjoint set -> 서로소 집합
// union-find
// find : 집합 찾기 -> 루트 노드까지 끝까지 찾음
const find_parent = (parent, x) => {
  if (parent[x] !== x) {
    parent[x] = find_parent(parent, parent[x]);
  }
  return parent[x];
};

// union : 두 원소가 속한 집합 합치기
const union_parent = (parent, a, b) => {
  a = find_parent(parent, a);
  b = find_parent(parent, b);
  if (a < b) parent[b] = a;
  else parent[a] = b;
};

const solution = () => {
  const [N, M] = input[0].split(" ").map(Number);
  const parent = Array.from({ length: N + 1 }, (_, i) => i);

  // 모든 원소에 대해 union 수행
  for (let i = 1; i <= M; i++) {
    const [a, b] = input[i].split(" ").map(Number);
    union_parent(parent, a, b);
  }

  let rootCount = new Map();
  for (let i = 1; i < N + 1; i++) {
    const root = find_parent(parent, i);
    // root node가 count가지면 그거 가져오고 없으면 0으로 대체, 발견된 거 +1 해서 갱신
    rootCount.set(root, (rootCount.get(root) || 0) + 1);
  }

  let total = 1;
  //위에서 저장한 rootCount의 value를 가져옴, 즉 위에서 갱신한 정점의 개수
  for (const size of rootCount.values()) {
    total = (total * size) % 1000000007;
  }
  console.log(total);
};

solution();
