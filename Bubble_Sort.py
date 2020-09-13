arr=[1,3,6,5,4,8,7,0]
isSorted=False
temp=0
while(not isSorted):
    isSorted=True
    for i in range(1,len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
print(arr)