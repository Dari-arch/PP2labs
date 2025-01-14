a='Hello'
b='World'
c="Hello World !"
d=a+b+"!"
print(a,b)
print(a+b+"!")
print(c[2:])
print(c[:5])
print(c[-5:-2])
print(c[0])
print(a.upper())
print(b.lower())
print(c.split(" "))
print(c.strip()) # removes any whitespace from the beginning or the end
print(a.replace("H","J"))
print(d)
if a.isdigit():
    print("Yes")
else:
    print("No")
print(a.count("l"))
