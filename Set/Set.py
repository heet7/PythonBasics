
l  = [ 1,1,1,'a','a'] # output: [ 1,1,1,'a','a']

# now we change it into set
l = set(l)
print(l)  #output : {1,'a'}

# Union
a = {1,2,3,'a'}
b = {3,4}
a.union(b) # output : {1,2,3,4,'a'}

# intercection
print( a & b ) #output : {5}

# A - B
print ( a - b ) # output: {1,2,'a'}

# B - A
print ( b - a ) # output: {4}
