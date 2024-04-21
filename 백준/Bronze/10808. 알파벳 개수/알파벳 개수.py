S = input()  # 입력 받는 단어 S

# 결과를 저장할 리스트
arr = []

# 알파벳 'a'부터 'z'까지 순회
for char in 'abcdefghijklmnopqrstuvwxyz':
    arr.append(S.count(char))  # 각 문자의 등장 횟수를 count 함수로 찾아서 리스트에 추가

# 결과 출력
print(" ".join(map(str, arr)))
