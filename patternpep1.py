n=int(input('enter the size of pattern : '))
arr=list(map(int,input('Enter the elements of the array : ').split()))
maxnum=max(arr)

for i in range(maxnum,0,-1):
    for j in range(0,len(arr)):
        if arr[j]>=i:
            print('*' , end=' ')
        else:
            print(end='  ')
    print(end='\n')        