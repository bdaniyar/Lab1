def myfunc():
  x = 300
  print(x)

myfunc()

#Example 2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Example 3
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Example 4
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())