# Local variable
def fun(x):
    var_now = 5
    return x + var_now
fun(10) #output will be 15

# but what if we access that variable from outside of the function
# Let's C what happen..
print(var_now)

# so we got this error..
# NameError: name 'var_now' is not defined

# --------------BUT------------------------
# what happen if the variable is global
# Global variable

var_now = 20

def fun(x):
    global var_now
    var_now = 5
    return x + var_now

fun(10) # output will be 15

print(var_now) # output will be 15
# now the out put is 5 because it take from global variable
