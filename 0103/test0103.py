n = int(input('숫자를 입력하세요:')) 

sum = 0
for i in range (0,n,2):
    sum+=i
    print (i,end = " ") 
    print(" ")     
        
print("짝수의 합 : ", sum)        
   