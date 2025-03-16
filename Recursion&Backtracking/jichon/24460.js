const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function recur(lotto, n) {
  if (n === 1) return lotto[0][0]; //그룹 중 제일 작은 거

  let mid = Math.floor(n / 2);
  let quadrants = [
    lotto.slice(0, mid).map((row) => row.slice(0, mid)),
    lotto.slice(0, mid).map((row) => row.slice(mid)),
    lotto.slice(mid).map((row) => row.slice(0, mid)),
    lotto.slice(mid).map((row) => row.slice(mid)),
  ];
  let winners = quadrants.map((q) => recur(q, mid));

  winners.sort((a, b) => a - b);
  return winners[1];
}

const solution = () => {
  let n = +input[0];
  let lotto = [];

  for (let i = 1; i <= n; i++) {
    lotto.push(input[i].split(" ").map(Number));
  }

  console.log(recur(lotto, n));
};

solution();
