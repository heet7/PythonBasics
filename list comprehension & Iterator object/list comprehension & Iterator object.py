# List comprehension
l = [1,2,3,4,,32,13,1.9999,10.0,3.2,1,4.2,132,1.3.5,0]
l2 = [i**2 for i in l]
#      ^   {    ^    }
#      |        |
# condition   where 
#              to 
#             apply

# Multiple condition at a time...
# check the given list have odd number or even number or decimal(float)

l2 = [ i for i in l if i%2 == 0] # for even number
l3 = [ i for i in l if i%2 == 1] # for odd  number
l4 = [ i for i in l if(i%2 != 0) and (i%2 !=1) ] # decimal number

#  == is check
#  != not equal too

# ---------------------------------------------------------------------------------------------------

# Iterator object
l = [1,2,54,465,46,546,546,543,21,320,56.0,321,.0,21,561,54.00,3221,10.999]
l2 = (i for i in l)
# run this code once and comment this 24 number line it's remember all the number you can access this all number by next() function
next(l2)

# ---------------------------------------------------------------------------------------------------
 
# [] = store the value
# () = just remember all the things

# let's take one example we gona a create a 10000000 number and run the loop and check the compile time into both function...

# using List comprehension
l = [ i for i in range(10000000)]
# check the time of compilation

# using Iterator object
l = ( i for i in range(10000000))
# check the time of compilation

# ---------------------------------------------------------------------------------------------------
# get the all iter values using the for loop
for i in range(100):
  print(next(12))

# which one you think memory afficiant...?

#  ---------------------------------------------------------------------------------------------------
# let's chedck how to get the value of iterator object in list...
l = [12,,121,24,654,321,3524,651,321]  # create list
l2 = (i for i in l)                    # iterat
l3 = list(l2)                          # to list
l4 = iter(l3)                          # to iterable object
next(l4)                               # get next one value
type(l4)                               # check the data type....
