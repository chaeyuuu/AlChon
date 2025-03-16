const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function binary(n) {
  let start = 0;
  let end = n;
  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    if (mid * mid < n) start = mid + 1;
    else end = mid - 1;
  }
  return start;
}
const solution = () => {
  let n = +input[0];
  console.log(binary(n));
};

solution();
