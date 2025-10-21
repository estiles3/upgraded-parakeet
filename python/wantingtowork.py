import re
arr = {"sku": "VA-43", "size": "5ft", "name": "Blue Sky", "description": "A great product!"}
new = []
pattern = re.compile(r'[^A-Za-z0-9_.]')

for x in arr:
    if (x == "description"):
        check = arr[x]
        check = check[:10]+"..."
        new.append([x,check])
        continue
    check = arr[x].lower()
    if (len(check) > 10):
        check = check[:10]+"..."
    check = pattern.sub('_', check)
    new.append([x,check])
print(new)