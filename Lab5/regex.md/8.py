import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
result = re.findall('[A-Z][^A-Z]*', file.read())
print(result)