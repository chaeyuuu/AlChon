const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let N = +input[0];
  let A = input[1].split(" ").map(Number);
  let B = input[2].split(" ").map(Number);

  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  let sum = 0;
  for (let i = 0; i < N; i++) {
    sum += A[i] * B[i];
  }

  console.log(sum);
};

solution();
