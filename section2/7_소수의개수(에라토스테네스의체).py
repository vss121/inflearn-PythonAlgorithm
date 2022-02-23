import sys
sys.stdin = open("input.txt", "r")
n = int(input())
ch = [0]*(n+1)
cnt=0
for i in range(2,n+1):
  if ch[i]==0:
    cnt+=1
    for j in range(i,n+1,i): # step값 활용하기!***
      ch[j]+=1

print(cnt)
'''
<<timelimit>> 비효율적
for j in range(i, n+1):
  if j%i==0:
    ch[j]+=1
'''
