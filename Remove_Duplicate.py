#without using list
s= input("Enter the string:")
'''
output=''
for ch in s :
    if ch not in output:
        output=output+ch
print(output)
'''
#with list
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
output = ''.join(l)
print(output)
