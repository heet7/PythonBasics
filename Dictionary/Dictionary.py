
my_dict = {'name':['a','b','c'],'marks':(1,2,3)}

# get the value using keys
my_dict['name'] # output : ['a','b','c']

# if you give the keys their will tell you a value


# Now we gona a 
# update
my_dict2 = {1:[1,2,3]}
my_dict.update(my_dict2) #output : {'name':['a','b','c'],1:[1,2,3]}

my_dict2 = {'name':['aa','bb','cc']}
my_dict2.update(my_dict) # output : {'name' : ['aa,'bb','cc'],1:[1,2,3]}

# Just append in update...

# once again some questions that you solve in your mind and try to get perfect output...:)
my_dict['name'] = my_dict # output will be...
my_dict.update(my_dict)   # output will be...?
