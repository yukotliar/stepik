new = []
for i in objects:
    new.append(id(i))
new = set(new)
print(len(new))