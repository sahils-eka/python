# class polym():
#     def poly(self, inp):
#         print(f"{inp} is your input and it's type is-> {type(inp)}")


# n = polym() poly poly
# s = polym()

# Poly

# n.poly(1)
# s.poly("Sahil")

### Treebo  ###
'''
lis = [2, 4, 7, 5, 3, 6, 1]
lis.sort()
print(lis)
j = len(lis) - 1
sum = 7
for i in range(len(lis)):
    pass
'''
# numdi = {1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2}
# # numdi_List = [numdi]
# numdiItems = list(numdi.items())

# numdiItems.sort(key=lambda x: x[1], reverse=True)
# print(numdiItems)
# numdi = dict(numdiItems)
# print(numdi)


# HCL question
'''
marks = [
    ('Swaraj', 90, 'Maths'),
    ('Jatin', 60, 'Maths'),
    ('Divya', 20, 'Science'),
    ('Seema', 75, 'Science')
]

marks.sort(key=lambda x: x[1])
print(marks)
'''
### Thales question ###
'''
l = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 2, 3, 4]
numDict = {}
for i in l:
    count = 0
    for j in l:
        if i == j:
            count += 1
    numDict[i] = count

print(f"Before--> {numDict}")

numList = list(numDict.items())

numList.sort(key=lambda x: x[1])

numDict = dict(numList)
print(f"After--> {numDict}")
'''

'''
import json
with open(r"finalizedBill", "r") as file:
    content = file.read()

# print(content)
# print(type(content))
content = json.loads(content)
# print(type(content))

print(content.get("description"))
print(content.get("xyz"))

contentKeys = list(content.keys())
print(contentKeys)

name = {"Name": "Sahil Singh"}
age = [(23, 24)]
pwd = [("password", 123)]

content.update(name)
content.update(age)
content.update(pwd)
print(content.get("Name"))
print(content.get(23))
print(content.get("password"))
contentKeys = list(content.keys())
print(contentKeys)

err = [12, "sahil"]
# errDict = dict(err)
# print(errDict)
# This will throw an error, anyday!

# Deleting key-value from a Dictionary
a = content.pop(23)
print(f"a will be the value of key, i.e. = {a}")
contentKeys = list(content.keys())
print(contentKeys)

q, w = content.popitem()
print(q, w)
'''

# fromkeys() -- used to create dict
li = ["x", "y"]
value = 25
alp = dict.fromkeys(li, value)
print(alp)

# setdefault()
theJson = {
    "eventType": "ConsumerCustomerBillFinalizationNotification",
    "headers": "hehehaehahe",
    "billId": "363457924966"
}

print(type(theJson))
x = theJson.setdefault("billId", "garbage")
y = theJson.setdefault("name", "Sahil Singh")
print(x)
print(y)
print(theJson)
'''
with open(r"finalizedBill", "r") as file:
    content = file.read()

# print(content)

content = open("openfile.txt", "r")
li = content.read()
print(li)
content.close()
'''
