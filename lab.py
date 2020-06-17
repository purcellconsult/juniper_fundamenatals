
var1,var2=4,5.75
print("Orignal numbers of var1 and var2 are {}, {}" .format(var1, var2))
print ("task one to swap the two variables")
var1,var2=var2,var1
print("new var1 is {}, new var2 is {}" .format(var1,var2))

if var1 > var2:
    print ("The larger number between var1 and var2 is {}" .format(var1))
else:
    print ("The larger number between var1 and var2 is {}" .format(var2))

str1,str2="This is string1","This is string 2"
if len(str1) > len(str2):
    print ("the larger string between str1 and str2 is {}" .format(str1))
else:
    print ("The larger string between str1 and str2 is '{}'" .format(str2))

for x in range(1,101):
    if x % 2==0:
        print(x, end=' ')
x=1
print()
print("while loop practise")
while x in range(1,101):
    if x % 2 ==0:
        print(x,end=" ")
    x+=1


print()
for x in range(3):
    for y in range(3):
        print('*', end=' ')
    print('')

print()
for x in range(6):
    for y in range(x):
        print('*', end=' ')
    print( )
