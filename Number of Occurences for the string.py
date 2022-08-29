s = input("Enter the string:")
#Using list
'''
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occcurs {} times'.format(ch,s.count(ch)))
'''
#Using Set
s1=set(s)
for ch in sorted(s):
     print('{} occurs {} times'.format(ch,s.count(ch)))
