# exception handling
def fun(x,y):
    
    try:
        c = x / y
        return c
    
    except:
        print("we got an error")
        
    finally:
        print("we will excute this part anyway")
        
        
fun(10,2)
# answer
# we will excute this part anyway
# 5.0

# fun(10,0)
# answer
# we got an error
# we will excute this part anyway
