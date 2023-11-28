// function solution(m, n, board) {
//     var arr = [...board];
//     let varArr = arr.map(function(item) {
//         return item.split('');
//     });
//     let ridArr = []
//     rid(varArr,ridArr,m,n)

// }

// function rid(varArr,ridArr,m,n){
//     for (let i = 0 ; i < m-1; i ++){
//         for (let j = 0 ; j < n-1; j ++ ){
//             if (varArr[i][j] === varArr[i+1][j+1] && 
//                 varArr[i][j] === varArr[i][j+1] && 
//                 varArr[i][j] === varArr[i+1][j]) {
//                 console.log(varArr[i][j])
//                 ridArr.push([i,j],[i+1,j],[i,j+1],[i+1,j+1])
//             } else {
                
//             }
//         }
//     }
//     for (let val of ridArr){
//         varArr[val[0]][val[1]] = ''
//     }
//     console.log(varArr,'board')
//     // 당겨주는 로직
    
//     pull(aaa)
//     // return red()
// }
function solution(m, n, board) {
  const boardArray = board.map(row => row.split(''));
  let answer = 0;

  while (true) {
    const blocksToRemove = new Set();

    // 2x2로 같은 블록 찾기
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        const currentBlock = boardArray[i][j];

        if (currentBlock === '0') {
          continue;
        }

        if (
          currentBlock === boardArray[i + 1][j] &&
          currentBlock === boardArray[i][j + 1] &&
          currentBlock === boardArray[i + 1][j + 1]
        ) {
          blocksToRemove.add(`${i},${j}`);
          blocksToRemove.add(`${i + 1},${j}`);
          blocksToRemove.add(`${i},${j + 1}`);
          blocksToRemove.add(`${i + 1},${j + 1}`);
        }
      }
    }

    // 더 이상 제거할 블록이 없으면 반복 종료
    if (blocksToRemove.size === 0) {
      break;
    }

    // 제거할 블록을 '0'으로 표시
    blocksToRemove.forEach(block => {
      const [i, j] = block.split(',').map(Number);
      boardArray[i][j] = '0';
    });

    // 제거한 블록의 개수 누적
    answer += blocksToRemove.size;

    // 블록 이동
    for (let j = 0; j < n; j++) {
      for (let i = m - 1; i >= 0; i--) {
        if (boardArray[i][j] === '0') {
          let k = i - 1;
          while (k >= 0 && boardArray[k][j] === '0') {
            k--;
          }

          if (k >= 0) {
            boardArray[i][j] = boardArray[k][j];
            boardArray[k][j] = '0';
          }
        }
      }
    }
  }

  return answer;
}
