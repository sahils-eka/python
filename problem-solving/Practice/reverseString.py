# import re

# # 1 output --> cerence is name My
# # 2 output --> ecnerec si eman yM


# def output1(str):
#     st1 = str.split(" ")
#     st1.reverse()
#     return " ".join(st1)


# def __output1(str):
#     st1 = re.findall(r'[1-9]+', str)
#     print(st1)


# st = "My name is cerence"
# assert output1(st) == 'cerence is name My', "Not the expected Output"

# try:
#     print(1/0)
# except Exception as error:
#     print(error)

# print(output1(st))
# __output1(st)

import requests

ur = "https://reqres.in/api/users"
pm = {"page": 1}
payload = {"email": "sahil@eka.com",
           "first_name": "Sahil", "last_name": "Singh"}
resp = requests.put(url=ur, data=payload, params=pm)
print(resp.url, "\n")
print(resp.status_code)
print("\n", resp.json())
re2 = requests.get(url=ur, params=pm)
print("\n", re2.json())
