import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
result = re.findall(r"[A-Z]{1}[a-z]+", file.read())
print(result)