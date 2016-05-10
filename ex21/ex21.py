def add(a,b) :  # defined def"add" ,
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a,b) :
    print "SUBTRACTING %d - %d " % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d " % (a,b)
    return a * b

def divide(a,b) :
    print " DIVIDING %d / %d" %(a, b)
    return a / b


print " Let's do some math with just functions!"

age = add(20,3)
height = subtract(75,3)
weight = multiply(91,2)
IQ = divide (200,2)

print "Age : %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, IQ)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(IQ, 2)))) # First circulumate is inside 

print "That becomes:", what, "Can you do it by hand?"