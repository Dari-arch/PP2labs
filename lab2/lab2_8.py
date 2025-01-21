list = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list)
print(type(list))
print(list2[2])
print(list3[1])
print(list2[-1])
print(list[1:])
print(list3[:2])
print(list2[1:2])
if "apple" in list:
  print("Yes, 'apple' is in the fruits list")
list[1] = "blackcurrant"
print(list)
list[1:3] = ["watermelon"]
print(list)
list.insert(2, "orange")
print(list)
list.append("orange")
print(list)
list.extend(list2)
print(list)
list.remove("orange")
print(list)
list.pop()
print(list)
list.pop(0)
print(list)
del list[0]
print(list)
list2.clear()
print(list2)
i = 0
while i < len(list):
  print(list[i])
  i = i + 1
for x in list3:
  print(x)
for i in range(len(list)):
  print(list[i])
[print(x) for x in list3]