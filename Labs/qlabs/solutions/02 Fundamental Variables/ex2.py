#!/usr/bin/python

# Create two variables, one containing your first name
first = 'Fred'
# and another containing your last name. 
last  = 'Bloggs'
# Display them using print.
print first,last

# Now transfer these variable values into a list
names = [first, last]; 
# display the list
print "names"

# Transfer these variable values into a dictionary, 
# using keys 'first' and 'last'.  
mydict = {'first' : first,
        'last'  : last}

# Display the values.
print mydict['first'], mydict['last']
