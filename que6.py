list_integer=[]
for i in range(1,5):
    user=int(input("Enter a number: "))
    if user>100:
        list_integer.append('over')
    else:
        list_integer.append(user)
    
print(list_integer)
   
    