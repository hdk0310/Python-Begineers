##### A python program to print 99 bottles of beer song

# Define a function 
def sing(n):

    if (n == 1):
        objects = 'bottle'
        objectMinusOne = 'bottles'

    elif (n == 2):
        objects = 'bottles'
        objectMinusOne = 'bottle'

    else:
        objects = 'bottles'
        objectMinusOne = 'bottles'
    
    
    if (n > 0):
        print (n , objects , "of beer on the wall", n ,objects ,"of beer")   
        print ("Take one down and pass it around", n-1,objectMinusOne, "of beer")       
    elif (n ==0):
        print ("No more bottles of beer on the wall, no more bottles of beer .")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print("Error: Wheres the booze?")
    
bottles = 99
while bottles >= 0:
    sing(bottles)
    bottles -=1    
