print "please Count people's number"
people = raw_input()

print "please Count car's number"
cars = raw_input()

print "please Count trucks's number"
trucks = raw_input()


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide"

if trucks > cars:
    print "That's tpp many trucks."
elif trucks < cars :
    print "Maybe we could take the trucks."
else:
    print " We still can't decide"

if people > trucks :
    print "Alright, let's just takd the trucks."
else:
    print  "Fine, let's stay home then."