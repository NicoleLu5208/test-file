condition=True
list=[]
while(condition):
            print('here is the list finding calculator')
            print("please add number into the list")
            number=int(input())
            print('would you like to add more?, if so input yes, if not input no')
            answer=input()
            if (answer=='yes'):
                list.append(number)
                condition=True
            else:
                list.append(number)
                condition=False

evenlist=[]
oddlist=[]

for i in range(len(list)):
    if(list[i]%2==0):
        print('even number',list[i])
        evenlist.append(list[i])
    
    else:
        print('odd number',list[i])
        oddlist.append(list[i])
        
print('the even list is',evenlist)
print('the odd list is',oddlist)
