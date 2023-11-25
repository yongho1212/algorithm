// function solution(land) {
//     const ans = [];
//     let idx = -1;
    
//     for (const i of land){
//         if (idx === -1){
//             // 해당행 최댓값
//             let maxNum = Math.max(...i);
//             ans.push(maxNum);
//             idx = i.indexOf(maxNum);    
//         } else {
//             // splice 로직 추가
//             let iArr = [...i]
//             let splicedArr = iArr.splice(idx,1);
//             let maxNum = Math.max(...iArr)
//             // console.log(iArr, splicedArr, maxNum)
//             ans.push(maxNum);
//             idx = [...i].indexOf(maxNum)
//         }
//     }
//     return ans.reduce((a,b) => a + b, 0)
//     // for 문 돌면서 
//     // 해당 행의 가장 큰 수 + 인덱스 값 저장
//     // 다음 for 문에서 인덱스 값 splice 
// }

function solution(land) {
    for(let i = 1; i < land.length; i++) {
        land[i][0] += Math.max(land[i - 1][1], land[i - 1][2], land[i - 1][3]);
        land[i][1] += Math.max(land[i - 1][0], land[i - 1][2], land[i - 1][3]);
        land[i][2] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][3]);
        land[i][3] += Math.max(land[i - 1][0], land[i - 1][1], land[i - 1][2]);
    }

    return Math.max(...land[land.length-1]);
}
