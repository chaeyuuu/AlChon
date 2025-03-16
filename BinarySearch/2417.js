const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let n = +input[0];
  let sq = Math.floor(Math.sqrt(n));
  //왜 Math.floor가 아니라 ~~를 썼을 때에는 오류일까?
  if (sq * sq < n) sq += 1;
  console.log(sq);
};

solution();
