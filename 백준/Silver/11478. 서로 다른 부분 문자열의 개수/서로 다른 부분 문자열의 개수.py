n = input()

ans = set()

for i in range(len(n)):
    for j in range(i+1, len(n)+1):
        
        ans.add(n[i:j])
print(len(ans))