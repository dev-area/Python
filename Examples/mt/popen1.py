import os

for line in os.popen('python myapp.py').readlines():
    print(line)
