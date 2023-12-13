function solution(numbers) {
    let arr = new Set();
    for ( let i = 0; i < numbers.length -1; i ++ ){
        for ( let j = i + 1; j < numbers.length; j ++){
            const aa = numbers[i]+numbers[j];
            arr.add(numbers[i]+numbers[j])
        }
    }
    const newArr = [...arr];
    newArr.sort((a,b) => a - b);
    return newArr
    
}