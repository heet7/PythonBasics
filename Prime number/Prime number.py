# Prime number simple program :)
def prime(x):
    if x <= 1: # or x == 1
        return "Not A Prime"
    elif x == 2:
        return "prime"
    for i in range(2,x//2+1): # +1 for range function because range function goas with end-1 so...we add that 
        if x % i == 0:        # the main logic is this .... x % i == 0:
            return "Not A Prime"
        return "Prime"

prime(11)

# now let's do small excercise...
# can we get a prime number in between 50 to 100

# it is work with only true false in return
# so,
def prime(x):
    if x <= 1: # or x == 1
        return False
    elif x == 2:
        return True
    for i in range(2,x//2+1): # +1 for range function because range function goas with end-1 so...we add that 
        if x%i == 0:
            return False
        return True

prime(14)

# let's get 50 to 100 in between prime number 

l = []
for i in range(50,101): # hear range(50,101) 101 because range(start,end-1)
    if prime(i):
        l.append(i)
print(l)
