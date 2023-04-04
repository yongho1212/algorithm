
function solution(clothes) {
    let obj = {};
    for (let i = 0; i < clothes.length; i++) {
        if (!obj[clothes[i][1]]) {
            obj[clothes[i][1]] = 1;
        } else {
            obj[clothes[i][1]]++;
        }
    }
    let combinations = 1;
    for (let key in obj) {
        combinations *= (obj[key] + 1);
    }
    return combinations - 1;
}