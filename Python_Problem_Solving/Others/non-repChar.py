st = "hhellooxyytzii"
li = []
for i in st:
    count = 0
    for j in st:
        if i == j:
            count += 1
    if count > 1 and i not in li:
        li.append(i)

print(li[len(li)-2])
