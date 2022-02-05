#k번째 수
import sys
sys.stdin = open("input.txt", "rt")

T= int(input())
for t in range(T):
  n, s, e, k = map(int, input().split()) #map()으로 한 줄에 있는 수 읽어들임
  a = list(map(int, input().split())) #한 줄에 있는 수들을 리스트로 받아들임 ***
  b = a[s-1:e] #s번째에서 e번째까지는 [s-1:e]임 ***
  b.sort() #sort()할 때 윗 줄과 합치지 말고 다른 줄로
  print("#%d %d" %(t+1, b[k-1])) #k번째는 인덱스로 [k-1], for문에서 첫번째는 0이니 출력은 [t+1]로



"""
sort

#1 list.sort()
: 원본의 리스트를 오름차순으로 정렬 (= list.sort(reverse=False) )
오름차순 = 숫자는 작은 수에서 큰 수로, 대소문자는 대문자 소문자 순으로, 
#2 list.sort(reverse=True)
: 원본의 리스트를 내림차순으로 정렬
#3 sorted(list) 오름차순 정렬
#4 sorted(list, reverse=True) 내림차순 정렬
"""
