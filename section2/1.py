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
    
    
"""map
map(함수, 반복 가능한 자료형), 반환값: map객체
ex)
result1 = list(map(int, [1.1,2.2,3.3]))
ex) 
def func_pow(x):
	return pow(x,5)
result2 = list(map(func_pow,[1,2,3]))
print(f'map(func_pow, 리스트)) : {result2}') 
ex)
result3 = list(map(math.ceil, [1.1,2.2,3.3]))
"""
#f-string : f'Hi, I am {name}, I am {job} and I like to use {language}.'
#input() 할 때 수로 받아들이려면 int(input())으로 하기
