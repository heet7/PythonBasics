# Factorial 
# let's create it...
# n! = 1 x 2 x 3 x x 5....!n
def factorial(x):
  if x == 0:
    return 1
  else:
    return factorial(x-1)*x
print(factorial(5))

# Fbonacci Sries
# n = 5
# n = 1 , 1 , 2 , 3 , 5 , 8...+n

def febonacci(x):
  if x == 1 or x == 2:
    return 1
  else:
    return febonacci(x-1) + febonacci(x-2)
febonacci(5)
