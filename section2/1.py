#k번째 약수

import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int,input().split())
cnt = 0
for i in range(1, n+1): #1~n까지는 (1,n+1)
  if n%i==0:
    cnt += 1
  if cnt == k:
    print(i)
    break
else: #break를 당하면 else안함/ 정상적으로 끝나면 else 함
    print(-1)
    
