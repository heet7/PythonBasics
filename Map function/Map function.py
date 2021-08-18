# single input map function...
l = [ 1,0,34,45,67]

# this function have 1 input what if input is multiple...

def fun(x):
    return x**2

c=map(fun,l)
next(c)    # gives us next 1 value
list(c)    # gives us the list of c

# ----------------------------------------------------------------------------
# multiple input map function...
# if the input is missed match then the eual index calculate and remain value are not consider.....

l = [ 1,0,34,45,67]
l2 = [ -1,0,-34,-45]

def fun(x , y):
    return x+y

c = map(fun,l,l2) #hear we give 2 input as like function want x = l and y = l2...

# ----------------------------------------------------------------------------
# what if we want that remains values then......!

# Sonlution is you gona set default value   -> def fun(x = 0 , y = 0 ) <- the remain value is considered...
