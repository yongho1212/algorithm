function solution(numbers) {
    const stack = [];
    const answer = new Array(numbers.length).fill(-1);

    for (let i = 0; i < numbers.length; i++) {
        // 스택이 있고 && 스텍 맨뒤의 맨뒤에 있는애가 현재 비교 요소보다 작으면 
        while (stack.length > 0 && numbers[stack[stack.length - 1]] < numbers[i]) {
            const index = stack.pop();
            answer[index] = numbers[i];
        }
        // 처음엔 스택이 없으니까 0번째 스택에 삽입
        stack.push(i);
    }

    return answer;
}