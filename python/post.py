import requests


print("hello")
url = 'https://jsonplaceholder.typicode.com/todos'
myobj = {'somekey': 'somevalue'}

x = requests.get(url)

print(x.status_code)
#print(x.json())
setup = []
for x in x.json():
    lists = []
    for y in x:
        lists.append([y,x[y]])
    setup.append(lists)
    print(lists)

strings = []
for x in setup:
    value = x[2][1]
    if (value[0] == "q"):
        strings.append(value)
print(strings)
