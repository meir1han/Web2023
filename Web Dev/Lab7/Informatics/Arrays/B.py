n = int(input())

arr = list(map(int, input().split()))[:n]

for i in arr:
    if(i%2==0):
        print(i, end=" ")