function solution(files) {
    return files.sort((a, b) => {
        const regEx = /^(\D+)(\d{1,5})(.*)$/;
        const matchA = a.match(regEx), matchB = b.match(regEx);
        const headA = matchA[1].toUpperCase(), headB = matchB[1].toUpperCase();
        const numberA = parseInt(matchA[2]), numberB = parseInt(matchB[2]);

        if (headA < headB) return -1;
        if (headA > headB) return 1;
        if (numberA < numberB) return -1;
        if (numberA > numberB) return 1;
        return 0;
    });
}
