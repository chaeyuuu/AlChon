const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

// disjoint set -> 서로소 집합
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

  let isCycle = false;
  let cyclenum = 0;

  for (let i = 1; i <= M; i++) {
    const [a, b] = input[i].split(" ").map(Number);
    // root가 똑같다 -> 돌고돈다는 말 아닌가!
    if (find_parent(parent, a) === find_parent(parent, b)) {
      isCycle = true;
      cyclenum = i;
      break;
    } else {
      union_parent(parent, a, b);
    }
  }

  console.log(cyclenum);
};

solution();
