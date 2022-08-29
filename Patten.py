row =int(input("Enter the number of row:"))
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
'''
for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
'''
for i in range(row):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
'''
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
'''
for i in range(row):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
'''
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
'''
for i in range(row):
    for j in range(row-i):
        print(j+1, end=" ")
    print()
'''
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
'''
for i in range(row):
    for j in range(i-row,-1):
        print(" ", end= " ")
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
'''
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5

'''
'''
for i in range(row):
    for j in range(row-i):
        print(" ", end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
'''
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
'''
'''
for i in range(row):
    for j in range(row-i):
        print("", end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
'''
'''
    * 
    * * 
   * * * 
  * * * * 
 * * * * * 
'''
'''
for i in range(row):
    for j in range(row-i):
        print("", end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
'''
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
'''
for i in range(row):
    for j in range(row-i):
        print("", end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(row):
    for j in range(i+1):
        print("", end=" ")
    for j in range(row-i):
        print('*',end=" ")
    print()
'''
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
 1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1 
'''
'''
for i in range(row):
    for j in range(row-i):
        print("", end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(row):
    for j in range(i+1):
        print("", end=" ")
    for j in range(row-i):
        print(j+1,end=" ")
    print()
'''
'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
'''
for i in range(row):
    for j in range(i+1):
        print("",end=" ")
    for j in range(row-i):
        print("*",end=" ")
    print()
'''
'''
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
'''
for i in range(row):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(row-i):
        print("*",end=" ")
    print()
'''