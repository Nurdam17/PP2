import re
file = open("/Users/damirnurmagambetov/Desktop/PP2 Labs/Lab5/regex.md/text.txt", "r")
result = re.sub(r'(?:_+)(\w)', lambda m: m.group(1).upper(), file.read())
print(result)