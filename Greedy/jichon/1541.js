const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let numbers = input[0].split(/[\+\-]/).map(Number); // [55, 50, 40]
  let operators = input[0].match(/[\+\-]/g) || []; // ['-', '+']
  let idx = 0;
  let isMinus = false;
  for (let i = 0; i < operators.length; i++) {
    if (operators[i] === "-") {
      idx = i;
      isMinus = true;
      break;
    }
  }
  let sum = 0;
  if (isMinus) {
    for (let j = 0; j < idx + 1; j++) {
      sum += numbers[j];
    }
    for (let k = idx + 1; k < numbers.length; k++) {
      sum -= numbers[k];
    }
  } else {
    for (let j = 0; j < numbers.length; j++) {
      sum += numbers[j];
    }
  }
  console.log(sum);
};

solution();
