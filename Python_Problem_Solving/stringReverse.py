def reverse(s):
    str = ""
    for i in s:
        str = i + str
        print(str)
    return str


def ulta(s):
    arr = s.split(" ")
    ultaStr = ""
    i = len(arr)
    while(i > 0):
        ultaStr += arr[i-1]
        ultaStr += " "
        i -= 1
    print(ultaStr)


s = "Sahil singh is cool"
# ulta(s)
# print("The original string  is : ", end="")
# print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

print(11/2)
print(11//2)
