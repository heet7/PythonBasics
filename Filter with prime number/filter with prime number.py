# prime number
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
# #1 method to get the numbers
l = []
for i in range(50,101): # hear range(50,101) 101 because range(start,end-1)
    if prime(i):
        l.append(i)
print(l)

# #2 method to get the numbers using filter
a = filter(prime,range(50,101))
print(a)
