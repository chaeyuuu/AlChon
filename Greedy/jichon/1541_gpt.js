const fs = require("fs");
const input = fs.readFileSync("./input.txt").toString().trim();

const solution = () => {
  const parts = input.split("-"); //-로 분리
  let total = parts[0].split("+").reduce((acc, cur) => acc + Number(cur), 0);
  //- 앞 부분을 +로 더함

  for (let i = 1; i < parts.length; i++) {
    //- 뒤부분을 일단 모두 더함
    const partSum = parts[i]
      .split("+")
      .reduce((acc, cur) => acc + Number(cur), 0);
    total -= partSum; // - 부분 모두 뺴줌
  }

  console.log(total);
};

solution();
