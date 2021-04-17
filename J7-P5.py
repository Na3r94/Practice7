def check(x):
    sen = []
    result = 0
    for i in range(1,x+1):
        if x % i == 0:
            sen.append(i)

    if len(sen) == 2 :
        result = 1
    else :
        result = 2
    return result    

c = int(input('Enter your number : '))
z = check(c)
if z == 1:
    print('True')
elif z ==2:
    print('False')

a =  int(input('Enter first number : '))
b =  int(input('Enter second number : '))
aval = []

for i in range(a,b+1):
    test = check(i)
    if test == 1:
        aval.append(i)

print(aval)