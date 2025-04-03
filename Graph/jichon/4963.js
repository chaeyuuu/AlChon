const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const directions = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
  [-1, -1],
  [-1, 1],
  [1, -1],
  [1, 1],
];

function bfs(map, x, y, h, w) {
  let queue = [[x, y]]; //시작 점
  map[x][y] = 0; //방문 완료

  while (queue.length) {
    let [cx, cy] = queue.shift(); //queue에서 탐색할 점 하나 뽑음

    for (let [dx, dy] of directions) {
      let nx = cx + dx; //탐색할 방향 하나씩
      let ny = cy + dy;

      if (nx >= 0 && nx < h && ny >= 0 && ny < w && map[nx][ny] === 1) {
        map[nx][ny] = 0; //방문 완료
        queue.push([nx, ny]); //다음으로 탐색할 점 넣기
      }
    }
  }
}

const solution = () => {
  let index = 0;
  while (true) {
    let [w, h] = input[index].split(" ").map(Number);
    if (w === 0 && h === 0) break;

    let map = Array.from(Array(h), () => Array(w).fill(0));
    let count = 0;

    for (let i = 0; i < h; i++) {
      let row = input[index + 1 + i].split(" ").map(Number);
      for (let j = 0; j < w; j++) {
        map[i][j] = row[j];
      }
    }

    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (map[i][j] === 1) {
          bfs(map, i, j, h, w);
          count++;
        }
      }
    }

    console.log(count);
    index += h + 1;
  }
};

solution();
