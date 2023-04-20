import requests
import yaml

# job_data = {}
# job_data["title"] = "Tale of Eka"
# # print(job_data)

# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)
# print(f'Get--{response.json()}')

with open('exa_yaml.yml', 'r') as file:
    configuration = yaml.safe_load(file)
print(type(configuration))
print(configuration)

# todo = job_data
# response = requests.put(api_url, json=todo)
# print(f'Put--{response.json()}')

# print(response.status_code)

# todo = job_data
# response = requests.patch(api_url, json=todo)
# print(f'Patch--{response.json()}')

# if response.status_code in range(100,200):
#     print(response.status_code)
# else:
#     print(f"Response code= {response.status_code}")