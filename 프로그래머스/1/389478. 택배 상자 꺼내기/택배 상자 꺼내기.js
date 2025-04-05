function solution(n, w, num) {
    // 해당 박스의 위치 계산
    const row = Math.floor((num - 1) / w);
    const isEvenRow = row % 2 === 0;
    const col = isEvenRow ? (num - 1) % w : w - 1 - (num - 1) % w;

    let count = 0;
    const totalRows = Math.ceil(n / w);

    for (let r = row; r < totalRows; r++) {
        const base = r * w;
        let boxNum;

        if (r % 2 === 0) {
            // 왼쪽 → 오른쪽
            boxNum = base + col + 1;
        } else {
            // 오른쪽 → 왼쪽
            boxNum = base + (w - col);
        }

        if (boxNum <= n) {
            count++;
        } else {
            break;
        }
    }

    return count;
}