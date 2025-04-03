const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function buildGraph(N, edges) {
  const graph = Array.from({ length: N + 1 }, () => []);

  for (const [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
  }
  graph.forEach((neighbors) => neighbors.sort((a, b) => a - b));

  return graph;
}

function dfs(graph, start, visited) {
  visited[start] = true;
  process.stdout.write(start + " "); //한줄에 출력해야됨...

  for (const neighbor of graph[start]) {
    if (!visited[neighbor]) {
      dfs(graph, neighbor, visited);
    }
  }
}

function bfs(graph, start) {
  const queue = [start];
  const visited = Array(graph.length).fill(false);
  visited[start] = true;

  while (queue.length) {
    const node = queue.shift();
    process.stdout.write(node + " ");

    //너비 우선 -> 그 같은 정점이랑 연결된 간선들 먼저 다 싹 봐야되니까.
    for (const neighbor of graph[node]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        queue.push(neighbor);
      }
    }
  }
}

const solution = () => {
  let [N, M, V] = input[0].split(" ").map(Number);
  const edges = input.slice(1).map((line) => line.split(" ").map(Number));

  const graph = buildGraph(N, edges);

  let visited = Array(N + 1).fill(false);
  dfs(graph, V, visited);
  console.log();
  bfs(graph, V);
};

solution();
