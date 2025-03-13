const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const recur = function (lotto, n) {
  if (n == 2) {
    let flat_lotto = lotto.toString().split(",").map(Number);
    flat_lotto.sort((a, b) => a - b);
    return flat_lotto[1];
  }

  n = n / 2;
  let lotto_1 = Array.from({ length: n }, () => Array(n).fill(0));
  let lotto_2 = Array.from({ length: n }, () => Array(n).fill(0));
  let lotto_3 = Array.from({ length: n }, () => Array(n).fill(0));
  let lotto_4 = Array.from({ length: n }, () => Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      lotto_1[j][i] = lotto[j][i];
      lotto_2[j][i] = lotto[j + n][i];
      lotto_3[j][i] = lotto[j][i + n];
      lotto_4[j][i] = lotto[j + n][i + n];
    }
  }

  let result_list = [];
  result_list.push(recur(lotto_1, n));
  result_list.push(recur(lotto_2, n));
  result_list.push(recur(lotto_3, n));
  result_list.push(recur(lotto_4, n));

  result_list.sort();
  return result_list[1];
};

const solution = () => {
  let n = +input[0];
  let lotto = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      lotto[j][i] = +input[j + 1].split(" ")[i];
    }
  }
  console.log(recur(lotto, n));
};

solution();
