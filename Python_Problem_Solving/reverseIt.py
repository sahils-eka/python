def reverseIt(s):
    l = list()
    l = s.split(" ")
    l = reversed(l)
    newStr = " ".join(l)
    print(newStr)


s = "Sahil singh is cool"
reverseIt(s)
