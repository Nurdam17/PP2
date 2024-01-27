import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
result = re.findall(r".*ab{2|3}.*", file.read())
print(result)