#K번째 큰 수
import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split()) 
card_num = list(map(int, input().split()))
res = set() #set자료형

for i in range(n-2): #첫번째~n-2번째까지
  for j in range(i+1,n-1): #i+1~n-1번째까지
    for m in range(j+1, n): #j+1~n번째까지 #k를 쓰면 중복됨
      res.add(card_num[i] + card_num[j] + card_num[m]) #set()에는 add
res = list(res)
res.sort(reverse=True) #set()자료구조를 list화 후 sort
print(res[k-1]) #[k-1]은 k번째

#for문 : range(start,stop,step) range붙이기

"""
for i in range(n):
  for j in (i+1,n):
    for m in (j+1, n): 도 가능
이라고 해도 n=5라고 하면 범위 (5,5) (6,5) 등은 어차피 실행이 안됨 
"""

"""
중복을 제거하려면? set

#집합 자료형 s1
set : 1) 중복X 2)순서X -> indexing X -> 인덱싱하려면 list(s1) 이나 tuple(s1) 이용
교집합 : s1 & s2 또는 s1.intersection(s2)
합집합 : s1 | s2 또는 s1.union(s2)
차집합 : s1 - s2 또는 s1.difference(s2)
값 1개 추가 : s1.add(4)
값 여러 개 추가 : s1.update([4,5,6])
특정 값 제거 : s1.remove(2)
"""
