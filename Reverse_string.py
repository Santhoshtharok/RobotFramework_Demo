s= input("Enter the string:")
rev_str =""
temp = s
for i in s:
    rev_str = i+rev_str
if rev_str == temp:
    print("String is Palandrome")
else:
    print("Not palindrome")