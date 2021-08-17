# function is very useful because the code written onece and it use multiple time....

# Go to direct excercise
def f(l):
  l1=[]
  l2=[]
  l3=[]
  for i in l:
    if i%2 == 0:
      l1.append(i)
    elif i%2 == 1:
      l2.append(i)
    else:
      l3.append(i)
  print(l1,l2,l3)
  
a = f([1,2,1.2,,12,4654,56,46,48,9,13,0.,32,1.0,52.2,32,0.2,3.2,32])
print(a)
# what is the output 

# output is a none why because you can check what is the difference between print and return statement by this link
# https://github.com/heet7/PythonBasics/blob/main/difference%20between%20return%20and%20print/ReadMe.md

