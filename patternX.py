n=int(input('Enter the size of the X : ' ))

for i in range(0,n):
    for j in range(0,n+1):
            if i==j or j==n-i-1:
                print('*',end=' ')
            else:
                print(end='  ')   

    print(end='\n')           
