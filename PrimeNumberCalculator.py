n = int(input("What number is being checked?"))
d = 2
while d < n:
  r = n%d
  if r ==0:
    print ("The number", n, "is not prime")
    d = n+1
  else:
    d = d+1
if d == n:
  print("The number", n, "is prime")
      
