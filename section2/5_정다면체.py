#정다면체
import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
cnt = [0] * (N+M+3) #    cnt라는 리스트 0으로 초기화 ***
max = -2147000000
for n in range(1, N+1):
  for m in range(1, M+1):
    cnt[n+m] += 1
for i in range(1, n+m+1):
  if cnt[i] > max:
    max = cnt[i]
for i in range(1, n+m+1):
  if cnt[i]==max:
    print(i, end =' ')

'''
실수 -> max는 아예 앞으로 뺴야 함
for ~
  max = 0
  if ~
    max = ~ 
'''
# 옆으로 출력하려면 print(무엇, end =' ')
# 리스트 0으로 초기화 : cnt = [0] * 개수
