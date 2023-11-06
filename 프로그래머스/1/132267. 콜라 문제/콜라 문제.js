function solution(a, b, n) {
    return getBottle(a, b, n, 0);
}

function getBottle(a, b, n, total) {
    if (n < a) return total;
    let newBottle = Math.floor(n / a) * b;
    let restBottle = n % a;
    return getBottle(a, b, newBottle + restBottle, total + newBottle);
}
