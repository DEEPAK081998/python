print("Enter the array : ")
arr=list(map(int,input().split()))
ele=int(input("Enter the element to be searched : "))
length=len(arr)

def binsrch(arr,ele,stindex,endindex):
    if endindex>=stindex:
    
        mid=stindex+int((endindex-stindex)/2)
        if ele==arr[mid]:
            return mid
    
        elif ele<arr[mid]:
            return binsrch(arr,ele,stindex,mid-1)
    
        elif ele>arr[mid]:
            return binsrch(arr,ele,mid+1,endindex)
    
    else:
        return -1

result=binsrch(arr,ele,0,length-1)
if result==-1:
    print("Element is not present in the array.")
else:
    print(f"Element is present at index : {result}")    
