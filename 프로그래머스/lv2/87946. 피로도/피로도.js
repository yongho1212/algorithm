function solution(k, dungeons) {
  let visited = Array(dungeons.length).fill(false);
  let ans = 0;

  let dfs = (hp, count, visited) => {
    ans = Math.max(ans, count); // 현재 count와 ans 중 최대 값을 ans에 저장합니다.

    for (let i = 0; i < dungeons.length; i++) {
      if (visited[i] || dungeons[i][0] > hp) {
        continue;
      }

      visited[i] = true;
      dfs(hp - dungeons[i][1], count + 1, visited);
      visited[i] = false;
    }
  };

  dfs(k, 0, visited); // 초기 호출

  return ans; // 계산된 정답 반환
}