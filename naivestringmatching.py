def string():
  s=input("Enter a text string : ")
  x=len(s)
  print('\n')
  a=input("Enter a desired string : ")
  y=len(a)
  print('\n')

  for i in range (0,x-y+1):
      for j in range(0,y):
         if s[i+j]!=a[j]:
             break;
         else:
             j+=1
      if j==y:
         print(f"String matched from index {i} to index {i+j-1}")
         break
      elif (i!=x-y+1):
         print("Strings not matched")
         break
      else:
         i+=1

print("***********Naive String Matching*********",end='\n\n')      
string()