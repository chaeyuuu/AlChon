const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const directions = [
  [0, 1],
  [1, 0],
  [-1, 0],
  [0, -1],
];

function bfs(map, x, y, N, M) {
  let queue = [[x, y]]; //시작 점
  map[x][y] = 0; //방문 완료

  while (queue.length) {
    let [cx, cy] = queue.shift(); //queue에서 탐색할 점 하나 뽑음

    for (let [dx, dy] of directions) {
      let nx = cx + dx; //탐색할 방향 하나씩
      let ny = cy + dy;

      if (nx >= 0 && nx < N && ny >= 0 && ny < M && map[nx][ny] === 1) {
        map[nx][ny] = map[cx][cy] + 1; //방문 완료
        queue.push([nx, ny]); //다음으로 탐색할 점 넣기
      }
    }
  }
}

const solution = () => {
  let [N, M] = input[0].split(" ").map(Number);

  let map = input.slice(1).map((line) => line.split("").map(Number)); //붙어서 입력은 이렇게 처리해야 된댕
  bfs(map, 0, 0, N, M);

  console.log(map[N - 1][M - 1] + 1); //맨 마지막 점까지
};

solution();
