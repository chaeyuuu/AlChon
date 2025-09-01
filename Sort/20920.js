const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const solution = () => {
  let [N, M] = input[0].split(" ").map(Number);
  let arr = {};

  for (let i = 0; i < N; i++) {
    const word = input[i + 1];
    if (word.length < M) continue;
    arr[word] = (arr[word] || 0) + 1;
  }

  const sorted = Object.entries(arr).sort((a, b) => {
    // 1) value 내림차순
    if (b[1] !== a[1]) return b[1] - a[1];
    if (a[0].length !== b[0].length) return b[0].length - a[0].length; // (문제 조건에 따라 길이 기준 있으면 추가)
    // 2) value가 같으면 key 사전순(오름차순) => localcompare는 무거움
    return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0;
  });

  //결과 한번에 모아서 출력
  let result = [];
  for (const [key] of sorted) {
    result.push(key);
  }
  console.log(result.join("\n"));
};

solution();
