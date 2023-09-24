function solution(A,B){
    A.sort(function(a,b){
        return a - b;
    });
    B.sort(function(a,b){
        return b - a;
    })
    let res = 0;
    for (let i = 0; i < A.length; i++){
        res += A[i] * B[i]
    }
    
    return res
}

