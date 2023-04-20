string = "978398156"
i = 0
li = []
z = 0
while i <= len(string):
    print("i= ", i, "z= ", z)
    print("string= ", string[i:i+z+1])
    st1 = len(str(string[i:i+z+1]))
    j = int(string[i:i+z+1])**2  # for iteration, to check the square of st1
    print("len of sq= ", len(str(j)))
    if i+len(str(j))+1 > len(string):
        if string[i+z+1:] is not None:
            li.append(string[i+z+1:])
        break
    elif j != int(string[i+st1:i+st1+len(str(j))]):
        print("Start from ", i+st1)
        print("Not Equal--> j=", j, "Num= ",
              int(string[i+st1:i+st1+len(str(j))]))
        li.append(string[i])
        i += 1
    else:
        print("Equal--> j=", j, "Num= ", int(string[i+st1:i+st1+len(str(j))]))
        z = 0
        if len(str(j)) == 1:
            z = 0
        else:
            z += len(str(j))-1  # help gets the base number st1
        i += 1
newString = "".join(li)
print("The String "+string+" after removing the series is: ", newString)
