#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:29:17 2017

@author: parallels
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:21:10 2017

@author: parallels
"""

# simple dictionary

import json

list = ['foo', {'bar': ('baz', None, 1.0, 2)}]
with open("dict.json",'w') as d:
    json.dump(list,d)


print list

#["foo", {"bar": ["baz", null, 1.0, 2]}]