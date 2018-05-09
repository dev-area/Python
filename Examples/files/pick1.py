import pickle
 
d1={'name':'liran', 'id':1000, 'age': 45}
 
outp = open('customer', 'wb')
pickle.dump(d1, outp)
outp.close()

inp = open('customer', 'rb')
cust = pickle.load(inp)
print(cust)
inp.close()
