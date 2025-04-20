 const fs = require("fs");
 const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
 const n = Number(input[0]);
 const positions = input.slice(1).map(line => {
   const [x, y] = line.split(" ").map(Number);
   return { x, y };
 });

function solution(n, positions){
  let ans = 0;
  let matrix = Array(100).fill().map(() => Array(100).fill(0));
  for (let i=0; i< n; i ++){
    for (let j = positions[i].y; j<positions[i].y + 10; j ++){
      matrix[j].fill(1, positions[i].x, positions[i].x + 10);
      
    }
  }
  for (let m=0; m< 100; m ++){
    let temp = matrix[m].filter(x => x === 1);
    ans += Number(temp.length)
  }
  return ans
}

console.log(solution(n, positions))