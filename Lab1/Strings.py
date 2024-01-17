#Ex1(Use the len function to print the length of the string.):
x = "Hello World"
print(len(x))

#Ex2(Get the first character of the string txt.):
txt = "Hello World"
x = txt[0]

#Ex3(Get the characters from index 2 to index 4 (llo).):
txt = "Hello World"
x = txt[2:5]

#Ex4(Return the string without any whitespace at the beginning or the end.):
txt = " Hello World "
x = txt.strip()

#Ex5(Convert the value of txt to upper case.):
txt = "Hello World"
txt = txt.upper()

#Ex6(Convert the value of txt to lower case.):
txt = "Hello World"
txt = txt.lower()

#Ex7(Replace the character H with a J.):
txt = "Hello World"
txt = txt.replace('H', 'J')

#Ex8(Insert the correct syntax to add a placeholder for the age parameter.):
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))