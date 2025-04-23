// m명당 서버 1대 필요
// 서버 1대는 k시간 이용가능

// 하루동안 서버 증설 횟수

// 메모이징
// 증설 카운트가 올라가면 k시간후에 무조건 반납




function solution(players, m, k) {
    let answer = 0;
    let currCnt = 0;
    let queue = Array(k).fill(0)
    
        for (let i = 0; i < players.length; i++) {
        // 1. Handle expired servers from the queue
        const expired = queue.shift();
        currCnt -= expired;
        
        // 2. Calculate required servers for current hour
        const tempNum = Math.floor(players[i] / m);
        const req = Math.max(0, tempNum - currCnt);
        
        // 3. Update answer and current server count
        answer += req;
        currCnt += req;
        
        // 4. Add current requirement to the queue
        queue.push(req);
    }
    return answer
    
}