arr = list(map(int, input("enter numbers:").split()))
target = int(input("enter target:"))
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])