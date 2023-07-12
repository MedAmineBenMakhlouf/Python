def Countdown(number):
    listOfnum= []
    if(number<0):
        for i in range(number,1):
            listOfnum.append(i)

        return None
    else:
        for i in range(number,-1,-1):
            listOfnum.append(i)
        return listOfnum
        
print(Countdown(10))

def Print_And_Return(list):
    if len(list)>2:
        print("a list must have 2 values")
    else:
        print(list[0])
        return list[1]
listOfNum = [1,2,3]    
second = Print_And_Return(listOfNum)
print(second)

def First_Plus_Length(list):
    sum = list[0]+len(list)
    return sum

listOfNumbers = [1,2,3,4,5]
sum = First_Plus_Length(listOfNumbers)
print(sum)

def Values_Greater_than_Second(list):
    if len(list)<2:
        return False
    else:
        newList = []
        value = list[1]
        print(value)
        for i in list:
            if i>value:
                newList.append(i)
        return newList

listOfNumbers = [5,2,3,2,1,4]
y = Values_Greater_than_Second(listOfNumbers)
print(y)


def length_and_value(a,b):
    listOfNumbers =[]
    for i in range(0,a):
        listOfNumbers.append(b)
    return listOfNumbers

ls = length_and_value(4,7)
print(ls)