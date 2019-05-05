
def getid(name):
    v = -1
    f = open('cust.csv')
    f.readline()
    ls = f.readlines()
    for i in ls:
        s = i.split(',')
        if name == s[1]:
            v = int(s[0])
            break
    f.close()
    return v
    
def fil(item,cid):
    return item.split(',')[1] == cid


def getorders(custid):
    f = open('orders.csv')
    f.readline()
    ls = f.readlines()
    ret = list(filter(lambda x:x.split(',')[1]==custid,ls))
#    ret = list(filter(lambda x:fil(x,custid),ls))
    f.close()
    return ret

def calcsum(ls):
    s = 0
    for i in ls:
        t = i.split(',')
        s+=int(t[3])
    return s


while True:
    x = input('enter name(q to exit):')
    if x == 'q':
        break
    i = getid(x)
    if i == -1:
        print('not found')
        continue
    orders = getorders(str(i))
    if len(orders) == 0:
        print("no orders")
        continue
    s = calcsum(orders)
    print("sum=",s)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    