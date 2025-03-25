const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let [N, M] = input[0].split(" ").map(Number);
  let num = input[1].split(" ").map(Number);

  let presum = new Array(N + 1).fill(0);
  presum[0] = num[0];
  for (let k = 1; k < N; k++) {
    presum[k] += presum[k - 1];
    presum[k] += num[k];
  }
  for (let k = 0; k < M; k++) {
    let [i, j] = input[k + 2].split(" ").map(Number);
    console.log(presum[j - 1] - presum[i - 1] + num[i - 1]);
  }
};

solution();
