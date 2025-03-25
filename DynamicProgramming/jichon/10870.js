const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function fibbonachi(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fibbonachi(n - 1) + fibbonachi(n - 2);
  }
}

const solution = () => {
  let num = +input[0];
  console.log(fibbonachi(num));
};

solution();
