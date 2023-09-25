function solution(n) {
    if (n === 1) return 1;
    let ans = 0;
    for (let i = 1; i <= n; i++){
        let temp = 0;
        let cnt = i;
        while (temp < n){
            temp += cnt;
            cnt ++
            if (temp === n){
                ans += 1
            }
            if (temp > n){
                break;
            }
        }
    }
    return ans
}