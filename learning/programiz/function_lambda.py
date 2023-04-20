lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 23},
       {"name": "Nikhil", "age": 19}]

lis.sort(key=lambda x: x["age"])

print(lis)
