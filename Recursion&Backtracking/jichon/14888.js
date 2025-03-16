const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

let result = [];

function permutation(arr, selectNum) {
  let result = [];
  if (selectNum === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permuationArr = permutation(restArr, selectNum - 1);
    const combineFixer = permuationArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
}

function recur(n, number, op_set) {
  for (let i = 0; i < op_set.length; i++) {
    let temp = number[0];
    for (let j = 0; j < n - 1; j++) {
      if (op_set[i][j] === "+") {
        temp += number[j + 1];
      } else if (op_set[i][j] === "-") {
        temp -= number[j + 1];
      } else if (op_set[i][j] === "*") {
        temp *= number[j + 1];
      } else if (op_set[i][j] === "/") {
        if (temp < 0) {
          temp = -Math.floor(Math.abs(temp) / number[j + 1]);
        } else {
          temp = Math.floor(temp / number[j + 1]);
        }
      }
    }
    result.push(temp);
  }

  console.log(Math.max(...result));
  console.log(Math.min(...result));
}

const solution = () => {
  let n = +input[0];

  let number = [];
  input[1].split(" ").forEach((item) => number.push(+item));

  let op = [];
  input[2].split(" ").forEach((item) => op.push(item));

  let op_list = [];
  let symbol = ["+", "-", "*", "/"];
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < op[i]; j++) {
      op_list.push(symbol[i]);
    }
  }

  let op_set = [...new Set(permutation(op_list, op_list.length))];
  recur(n, number, op_set);
};

solution();
