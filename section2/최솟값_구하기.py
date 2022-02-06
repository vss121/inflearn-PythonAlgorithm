#최솟값 구하기

#1
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') #가장 큰 값으로 초기화함 
for i in range(len(arr)):
  if(arr[i] < arrMin): # <이면 처음의 값, <=이면 나중의 값
    arrMin = arr[i]
print(arrMin)

#2
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for i in range(1,len(arr)):
  if(arr[i] < arrMin):
    arrMin = arr[i]
print(arrMin)

#3
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') 
for x in arr:
  if x < arrMin:
    arrMin = x
print(arrMin)
