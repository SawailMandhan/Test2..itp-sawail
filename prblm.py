#firstly define the list according according to program
phoneDirectory={}
#print the following everytime ask choice
option=0
while(option!=5):
 print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
 print("1.Add a record\n")
 print("2.update a record\n")
 print("3. search a record\n")
 print("4.delete a record\n")
 print("5.Quit")
 #print choice
 option=int(input("Enter your choice: "))
 #In option 1 we have to add the record 
 if (option==1):
  a=input("Enter name:")
  b=int(input("Enter your 10-digit phone number:"))
  #  list
  phoneDirectory.update({a:b})
   #display message
  print("Record added")
 #In option 2 we can update it  
 elif (option==2):
  a=input("Enter name:")
  b=int(input("Enter your 10-digit phone number :")) 
   #  list
  phoneDirectory.update({a:b})
   #display message
  print("record updated")
#In option 3 we can search  it  
 elif (option==3):
  a=input("Enter name to search:")
  x=0
  for j in phoneDirectory.keys():
   if (j==a):
      #  list
    print(j,":",phoneDirectory[j])
    x=1
   else:
    pass
  if(x==0):
    # if record not found display this message 
    print("Not found")
 #In option 4 we can delete it   
 elif (option==4):
  a=input("Enter name:")
   #for deleting product
  phoneDirectory.pop(a)
    #display message
  print("record DEleted")
 
print("quit!!")
#print dictonary
print(phoneDirectory)