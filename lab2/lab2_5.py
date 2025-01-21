class myclass(): # class with no __len__ method
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))