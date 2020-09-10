def binary_search(arr,x):
    left=0
    right=len(arr)-1
    
    while(left<=right):
        mid=(left+right)//2
        if x==arr[mid]:
            return True
        elif x<arr[mid]:
            right=mid-1
        else:
            left=mid+1
    return False

arr=[1,2,3,4,5,6,7,8]
x=int(input("Enter a value to Search "))
if binary_search(arr,x):
    print("Found")
else:
    print("Not Found")