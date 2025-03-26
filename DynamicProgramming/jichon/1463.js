const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function dp(n, count) {
  if (n < 2) {
    return count;
  }
  return Math.min(
    dp(~~(n / 2), count + 1 + (n % 2)),
    dp(~~(n / 3), count + 1 + (n % 3))
  );
}

const solution = () => {
  let num = +input[0];
  console.log(dp(num, 0));
};

solution();
