#Example 1
try:
  print(x)
except:
  print("An exception occurred")

#Example 2
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Example 3
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Example 4
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

  