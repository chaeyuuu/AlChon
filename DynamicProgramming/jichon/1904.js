const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function dp(n) {
  let dp = Array(n + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
  }
  return dp[n];
}

const solution = () => {
  let num = +input[0];
  console.log(dp(num));
};

solution();
