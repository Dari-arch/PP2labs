x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc() # Python is fantastic

print("Python is " + x) # Python is awesome. Because we have a global variable x = "awesome" and a local variable x = "fantastic" in the function myfunc().