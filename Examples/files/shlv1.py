import shelve
 
s=[1,2,3,4]
 
outp = shelve.open('customer.dat')
outp['c1'] = s
outp.close()
 
inp = shelve.open('customer.dat')
d = inp['c1']
print(d)
inp.close()
