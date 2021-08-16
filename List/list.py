# l[start : end+1 : step size]

l = [ 1,2,3,"sam",[1,2,9],True]

# indexing and slcing the list
l[ : : -1] #reverse full string

# why it is mutable..
l[0] = 5
print(l)

# now we can change the words of the string.... which is actually immutable thing
a = 'pam'
b = list(a) # convert into list
b[0] = 's'  # chage the value of list
"{}".join(b) #marge togather with {}. =>'s{}a{}m'

# add & remove method
l = [1,2,3,5,6]
l.append(3) # [1,2,3,5,6,3]
l.remove(1) # [2,3,5,6,3] remove work with present value into list
l.pop(0) # [3,5,6,3] pop work with index...

# concatenate 
l1 = [1,2,3]
l2 = [7,6]

print(l1+l2) #add both list togather = [1,2,3,7,6]
print(l1*2)  #it's gives us the two time l1 = [1,2,3,1,2,3]

# Excercise again i give you small task and you gona dry run program and get the output...
# what if
a = [1,2,3]
a.append([1,2,3])
print(a) # what is the value of a = ?

# what if
a + [4,5]
print(a) # what is the value of a = ?

# what if 
a.append(a)
print(a) # what is the value of a = ?

# this is the last one ok ...:) what if 
a = [1,2,3]
a.append([1,2,3])
a.append(a)
print(a) # what is the value of a = ?
