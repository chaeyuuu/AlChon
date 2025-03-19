const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function binary(dot, target, index) {
  let start = 0;
  let end = dot.length - 1;
  let result = -1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (dot[mid][index] < target) {
      start = mid + 1;
    } else if (dot[mid][index] === target) {
      result = mid;
      break;
    } else {
      end = mid - 1;
    }
  }
  return result;
}

const solution = () => {
  let n = +input[0];
  let [width, height] = input[1].split(" ").map(Number);
  let dot = [];
  for (let i = 2; i < n + 2; i++) {
    dot.push(input[i].split(" ").map(Number));
  }
  dot.sort((a, b) => a[0] - b[0]);

  let count = 0;
  for (let i = 0; i < n; i++) {
    let [x, y] = dot[i];
    let x_idx = binary(dot, x + width, 0);
    if (x_idx === -1) continue;
    let y_idx = binary(dot, y + height, 1);
    if (y_idx === -1) continue;

    let width_idx = dot.find(([dx, dy]) => dx === x + width && dy === y);
    let height_idx = dot.find(([dx, dy]) => dx === x && dy === y + height);

    if (width_idx && height_idx) count++;
  }

  console.log(count);
};

solution();
