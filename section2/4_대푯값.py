#대푯값
import sys
sys.stdin = open("input.txt", "r")
N = int(input())
score = list(map(int, input().split()))
avg = round(sum(score)/N)
'''
avg = sum(score)/N
avg = avg + 0.5
avg = int(avg)
'''
min = 2147000000
for idx, x in enumerate(score):
  tmp = abs(x-avg) #tmp에 간격을 저장 ***
  if tmp<min:
    min = tmp #떨어진 간격을 저장
    minScore = x #점수도 저장!
    res = idx+1
  elif tmp == min: # [19, 21] 처럼 앞 뒤로 간격이 같을 때도 생각 
    if x>minScore: # >일 경우 맨 처음 수, >=일 경우 중복되는 맨 나중 수
      minScore = x
      res = idx +1
print(avg, res) 

"""
반올림, 내림, 올림

#1 반올림
round(3.1415) #결과=3 소수 첫째 자리에서 반올림
round(3.1415, 2) #결과=3.14 소수 셋째 자리에서 반올림
round(31.415, -1) #결과=30
round(4.5) #결과 4 / round half to even / 반올림할 자리의 수가 5 -> 앞자리 숫자 짝수면 내림
round(4.511) #5
round(3.5) #결과 4 / " -> 앞자리 숫자 홀수면 올림

#2 내림
import math
math.floor(3.14)

#3 올림
import math
math.ceil(3.14)
"""

'''
round half up 방식으로 반올림 하는 방법
a= 66.6
a= a+0.5
a= int(a)

'''

"""
#for에서 enumerate
for index, value in enumerate(t):
"""
