const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const directions = [
  [2, 1],
  [1, 2],
  [-1, -2],
  [-2, -1],
  [2, -1],
  [1, -2],
  [-1, 2],
  [-2, 1],
];

function bfs(map, x, y, I) {
  let queue = [[x, y]]; //시작 점
  map[x][y] = 1; //방문 완료

  while (queue.length) {
    let [cx, cy] = queue.shift(); //queue에서 탐색할 점 하나 뽑음

    for (let [dx, dy] of directions) {
      let nx = cx + dx; //탐색할 방향 하나씩
      let ny = cy + dy;

      if (nx >= 0 && nx < I && ny >= 0 && ny < I && map[nx][ny] === 0) {
        map[nx][ny] = map[cx][cy] + 1; //방문 완료
        queue.push([nx, ny]); //다음으로 탐색할 점 넣기
      }
    }
  }
}

const solution = () => {
  let index = +input[0];

  for (let i = 0; i < index; i++) {
    let I = +input[1 + 3 * i];

    let map = Array.from(Array(I), () => Array(I).fill(0));

    let [sx, sy] = input[2 + 3 * i].split(" ").map(Number);
    let [ex, ey] = input[3 + 3 * i].split(" ").map(Number);

    bfs(map, sx, sy, I);

    console.log(map[ex][ey] - 1); //시작점도 방문 개수로 쳐서 그런 듯 싶은데..
  }
};

solution();
