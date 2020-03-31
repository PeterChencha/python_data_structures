class MyArray(object):
  def __init__(self):
    self.length = 0
    self.data = {}

  def get(self, index):
    return self.data[index]

  def random(self):
    return (" This is a random string ")

  def add(self, value):
    self.data[self.length] = value
    self.length =+ 1

  def removeFirstValue(self):
    pass


arr = MyArray()
arr.add(10)
arr.add(50)
#print (arr.random())
print (arr.get(1))
