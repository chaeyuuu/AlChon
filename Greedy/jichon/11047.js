const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function binary(k, a) {
  let start = 0;
  let end = a.length - 1;
  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    if (a[mid] <= k) start = mid + 1;
    else end = mid - 1;
  }
  return end;
}

const solution = () => {
  let [n, k] = input[0].split(" ").map(Number);
  let a = [];
  for (let i = 1; i < n + 1; i++) {
    a.push(+input[i]);
  }
  let countSum = 0;
  while (k > 0) {
    let idx = binary(k, a);
    let coin = a[idx];
    let count = Math.floor(k / coin);
    countSum += count;
    k -= count * coin;
  }

  console.log(countSum);
};

solution();
