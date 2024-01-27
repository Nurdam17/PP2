import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
result = re.sub(r"(\w)([A-Z])", r"\1 \2",file.read())
print(result)