import os

x=os.fork()
if x:
    print('hello parent')
else:
    print('hello child')
