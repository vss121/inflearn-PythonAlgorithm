import sys
sys.stdin = open("input.txt", "r")
N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  while x>0: # while 옆의 조건이 참이면 실행임
    sum += x%10
    x = x//10 # x//10이 아니라 x = x//10 임
  return sum
'''
또는
def digit_sum(x):
  sum=0
  for i in str(x):
    sum +=int(i)
  return sum
'''
max = -2147000000 #반복문 안에 max값을 초기화하면 안됨 #float('-inf')
for x in nums:
  tot = digit_sum(x)
  if tot>max:
    max = tot
    max_num = x

print(max_num)
