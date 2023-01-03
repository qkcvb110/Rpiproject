n=int(input('숫자를 입력해주세요.:'))
sum = 0
for i in range(0, n+1, 2):
    # print(i)
    if i%2 == 0:
        sum+= i
print(sum)