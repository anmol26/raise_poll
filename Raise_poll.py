
poll_msg= input("Enter your poll message: ")             #Chai Break time??
options= int(input("How many options are there? "))      #3
opt={}
for i in range(1,options+1):
    opt[i]=input("Enter Option "+ str(i)+": ")           #{1:"yes", 2:"no", 3:"may be"}
    
total=int(input("How many members are there? "))         #10

votes=dict.fromkeys(range(1,options+1),0)                #{1:0,2:0,3:0}
#print(votes)
names={}
print("    !!! Let's start voting !!!   ")
for j in range(1,total+1):
    name=input("Enter your name: ")
    vote=int(input("Hello "+name+" ,Which option do you want to vote for? "))
    names[name]=vote
    votes[vote]+=1
print()
print("   !!! Its result time !!!   ")
for k in range(1,options+1):
    print(opt[k]+": "+str((votes[k]/total)*100)+"%")   
print()


#print(names)
