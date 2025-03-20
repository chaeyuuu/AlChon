const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function available(job, k) {
  let total = 0;
  for (let i = 0; i < job.length; i++) {
    total += k;
    if (total > job[i]) return false;
  }
  return true;
}
// 더 간결..
// const canWork = (k) => job.every((deadline, i) => k * (i + 1) <= deadline);

function binary(job) {
  let [start, end] = [1, job[job.length - 1]];

  while (start <= end) {
    let mid = Math.floor((end + start) / 2);
    available(job, mid) ? (start = mid + 1) : (end = mid - 1);
  }
  return end; // 제일 큰 놈
}

const solution = () => {
  let job = input[1]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  console.log(binary(job));
};

solution();
