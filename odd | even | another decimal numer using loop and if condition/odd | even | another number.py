l=[1,2,3,50,12,3,4,56,6,84,54,35,65]
l2=[]
l3=[]
l4=[]

for i in l :
  
  if i%2 == 1:
    l2.append(i)
    return l2
  
  elif i%2 == 0:
    l3.append(i)
    return l3
  
  else:
    l4.append(i)
    return l4
   
