import json
from collections import namedtuple

jstr = '{"name":"eli","age":20}'

p = json.loads(jstr, 
               object_hook=lambda d: 
                   namedtuple('Person', d.keys())(*d.values()))
print (p.name,p.age)

p2 = p.__class__(30,'avi')

print (p2.name,p2.age)

