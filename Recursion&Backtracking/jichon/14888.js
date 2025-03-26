const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let n = Number(input[0]);
let numbers = input[1].split(" ").map(Number);
let operators = input[2].split(" ").map(Number);

let maxResult = -Infinity;
let minResult = Infinity;

function backtrack(idx, currentValue, plus, minus, multi, divide) {
  if (idx === n) {
    maxResult = Math.max(maxResult, currentValue);
    minResult = Math.min(minResult, currentValue);
    return;
  }

  if (plus > 0) {
    backtrack(
      idx + 1,
      currentValue + numbers[idx],
      plus - 1,
      minus,
      multi,
      divide
    );
  }
  if (minus > 0) {
    backtrack(
      idx + 1,
      currentValue - numbers[idx],
      plus,
      minus - 1,
      multi,
      divide
    );
  }
  if (multi > 0) {
    backtrack(
      idx + 1,
      currentValue * numbers[idx],
      plus,
      minus,
      multi - 1,
      divide
    );
  }
  if (divide > 0) {
    let newValue =
      currentValue < 0
        ? -Math.floor(Math.abs(currentValue) / numbers[idx])
        : Math.floor(currentValue / numbers[idx]);

    backtrack(idx + 1, newValue, plus, minus, multi, divide - 1);
  }
}

const solution = () => {
  backtrack(
    1,
    numbers[0],
    operators[0],
    operators[1],
    operators[2],
    operators[3]
  );
  console.log(maxResult === 0 ? 0 : maxResult);
  console.log(minResult === 0 ? 0 : minResult);
};

solution();
