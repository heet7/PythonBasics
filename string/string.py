# how to change the value using index

x="sam"
x[0]='p' # this is the wrong because the length of the string is not equal...
x='pam' # this is the right method because in this the size is equal
print(x)

# what if
x='sam'
x.upper()  #this means all the latter of string is convert into UPPER CASE
x.lower()  #this means all the latter of string is convert into lower case
x.capitalize()  #this means all the latter of string is convert into Capitalize

# How to get index by word?
x = 'sam python sam'
x.index('python') # it is giving you only index of the first letter which is in the string and if the word is repated then it is give the index of the first object...
# answer is 
x.index('sam')
# anwer is = 0
# what if the word isn't in the string then
x.index('samabdce')
# output = it will show you an error that ERROR : substring not found 

# how to check how many time word is repate in the index?
x.count('word name')
x.count('sam')
# output = 2

# indexing and slicing
x[start:end+1:step size]
x[ 1 :  : -1] # -1 = print negative side so the out put will be 'nohtyp mas'
x[   :10: -1] # 'mas'
x[   :  : -1] # it will print the full string in backword direction
       ^
       |
# this fields like start and end is gives us walking style...

# Type casting 
# ==> str to int
x = '12'
x = int(x)
print(x+1) # answer = 13
#  we got error when string have integer with another data type...

# small excercise you gona a dry run this 3 line of code that what will be the output ....
x = 12 
x = str(x)
print(x+'1')
# output = ?

