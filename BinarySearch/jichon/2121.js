const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let n = +input[0];
  let [width, height] = input[1].split(" ").map(Number);
  let dot = new Set();

  for (let i = 2; i < n + 2; i++) {
    dot.add(input[i]);
  }

  let count = 0;

  for (let d of dot) {
    let [x, y] = d.split(" ").map(Number);

    if (
      dot.has(`${x + width} ${y}`) &&
      dot.has(`${x} ${y + height}`) &&
      dot.has(`${x + width} ${y + height}`)
    ) {
      count++;
    }
  }

  console.log(count);
};

solution();
