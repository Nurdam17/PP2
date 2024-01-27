import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', file.read())
result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
print(result)