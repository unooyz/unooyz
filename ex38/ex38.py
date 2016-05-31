ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 1-things in that list. Let's fix that. ")

stuff = ten_things.split(' ') #
more_stuff = ["Day","Night","Song", "Frisbee", "Corn","Banana", "Girl", "Boy"]

while (len(stuff)) != 10:
    next_one = more_stuff.pop()  # next one
    print ("Adding: %s" % next_one)
    stuff.append(next_one)
    print("There as %d times now." % len(stuff))

print("There we go :%s" % str(stuff))
print("Let's do some things with stuff")

print("stuff[1] = %s" % stuff[1])
print("strff[-1] =  %s" % stuff.pop())
print(' '.join(stuff))
print('#'. join(stuff[3:5]))  # 3~ 4 (5 = front of 5)