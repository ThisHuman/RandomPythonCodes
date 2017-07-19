n = int(input("What number is being checked?"))
d = int(input("What number will divide it?"))
r = n%d
if r == 0:
  print ("The number", n, "is divisible by", d)
else:
  print("The number", n, "is not divisible by", d)
