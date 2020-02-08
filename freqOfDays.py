days=['mon','tues','wed','thurs','fri','sat','sun']

output=[4,4,4,4,4,4,4]

a=int(input(" Enter the number of inputs : "))
c=[None]*a
d=[None]*a
print("\n A week for me is :")
print( *days)
print("\n Enter number of days in the month <space> the day on the 1st day of the month : ")
for i in range(0,a):
    c[i],d[i]=input().split()
    c[i]=int(c[i])
    
def count(int,str):
    i=days.index(str)    
    if int==28:
        print(*output)
    if int==29:
        output[i]=5
        print(*output)
    if int==30:
        if str!='sun':
            output[i]=5
            output[i+1]=5
            print(*output)
        else:
            output[i]=5
            output[0]=5
            print(*output)
    if int==31:
        if str!='sat' and str!='sun':
            output[i]=5
            output[i+1]=5
            output[i+2]=5
        elif str=='sat':
            output[i]=5
            output[i+1]=5
            output[0]=5
        else:
            output[i]=5
            output[0]=5
            output[1]=5
        print(*output)   

#print("\n")
print("\n The month looks like : ")
for i in range(0,a):
    count(c[i],d[i])