s=input("Enter the word:")
#Reverse the word
'''
l=s.split()
l1=l[::-1]
outout =" ".join(l1)
print(outout)
'''
#reverse the each content of the word
'''
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
output=' '.join(l1)
print(output)
'''
#Reverse every second word in the given string:
l=s.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)