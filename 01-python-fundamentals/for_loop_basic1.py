for i in range(0,151):
    print(i)

print("---------------------------")
for i in range(5,1001):
    if i%5==0:
        print(i)

print("---------------------------")

for i in range (1,101):
    if i % 10 == 0  :
        print("Coding Dojo")
    elif i % 5 == 0 :
        print("Coding")
    else:
        print(i)

print("---------------------------")
sum=0
for i in range(0,500001):
    if i%2!=0:
        sum+=i
print(sum)

print("---------------------------")

for i in range(2018,-1,-4):
    print(i)

print("---------------------------")

def Flex(lowNum,highNum,multi):
    for i in range(lowNum,highNum+1):
        if i%multi==0:
            print(i)
    return None

Flex(2,9,3)
