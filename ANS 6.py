x=int(input("Enter the number:"))
count=1
while x!=0:
    
         r=x%10
         if count==2:
            break
         x//=10
         count+=1
print("The middle digit of the number is",r)    