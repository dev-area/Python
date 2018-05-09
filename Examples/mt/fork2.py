import os

ret=0
# we need to do something complex so lets create a child
x=os.fork()
if x:
    print('do half work by parent')
    ret = os.wait()
else:
    print('do half work by child')
    os._exit(10)

print("only parent here res=" + str(os.WEXITSTATUS(ret[1])))
