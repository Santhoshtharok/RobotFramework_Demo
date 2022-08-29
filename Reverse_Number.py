num=int(input("Enter the number:"))
rev_num = 0
temp =0
while(num>0):
    digit = num%10
    rev_num = (rev_num*10)+digit
    num =num//10
print(rev_num)