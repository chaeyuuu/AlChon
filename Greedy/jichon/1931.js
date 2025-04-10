const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let n = +input[0];
  let meetings = [];
  for (let i = 1; i < n + 1; i++) {
    let [start, end] = input[i].split(" ").map(Number);
    meetings.push({ start, end });
  }
  //끝나는 시간 기준으로 정렬 어케하지.. -> gpt 도움
  meetings.sort((a, b) => {
    if (a.end === b.end) return a.start - b.start;
    return a.end - b.end;
  });

  let count = 0;
  let lastEnd = 0;

  for (const { start, end } of meetings) {
    if (start >= lastEnd) {
      count++;
      lastEnd = end;
    }
  }
  console.log(count);
};

solution();
