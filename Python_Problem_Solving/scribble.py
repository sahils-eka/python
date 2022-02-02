string = "1232416256655369874"
i = 0
li = []
z = 0
while i <= len(string):
    st1 = len(str(string[i:i+z+1]))
    j = int(string[i:i+z+1])**2
    if i+len(str(j))+1 > len(string):
        if string[i+z+1:] is not None:
            li.append(string[i+z+1:])
        break
    elif j != int(string[i+st1:i+st1+len(str(j))]):
        li.append(string[i])
        i += 1
    else:
        z = 0
        if len(str(j)) == 1:
            z = 0
        else:
            z += len(str(j))-1
        i += 1
newString = "".join(li)
print("The String "+string+" after removing the series is: ", newString)
