# Chapter 5 Exercise 3
# Apply changes to a dictionary
             
machines = {'user100': 'yogi',
            'user1'  : 'booboo',
            'user2'  : 'rupert',
            'user3'  : 'teddy',
            'user4'  : 'care',
            'user5'  : 'winnie',
            'user6'  : 'sooty',
            'user7'  : 'padders',
            'user8'  : 'polar',
            'user9'  : 'grizzly',
            'user10' : 'baloo',
            'user11' : 'bungle',
            'user12' : 'fozzie',
            'user13' : 'huggy',
            'user14' : 'barnaby',
            'user15' : 'hair',
            'user16' : 'greppy'}

# (a)	user14 no longer has a machine assigned
machines['user14'] = None
 
# (b)	The name of user16's machine is changed to 'cinnamon' 
machines['user15'] = 'cinnamon'

# (c)	user16 is leaving the company,
# and a new user, user17, will be assigned his machine
machines['user17'] = machines['user16']
del machines['user16']
 
# (d)	user4, user5, and user6 are all leaving at exactly the same time,
# but their machine names are to be stored in a list called unallocated.
unallocated = []
for user in ('user4', 'user5', 'user6'):
    unallocated += [machines.pop(user)]

# (e) user8 gets another machine called 'kodiak' in addition to the one they already have.
machines['user8'] = [machines['user8'],'kodiak']

# (f)	Print a list of all the users, with their machines, in any order.
for kv in machines.items():
    print kv

print

# (g)	Print a list of unallocated machines, sorted alphabetically.
print "Unallocated machines:",sorted(unallocated)

 

