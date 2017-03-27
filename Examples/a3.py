# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 22:59:20 2015

@author: liran
"""

import sys
sequence = sys.argv[1]
#new_sequence = sequence.replace("T", "U")
#newer_sequence = new_sequence.replace("t", "u")
print sequence.replace("T", "U").replace("t", "u")
''''''''''''''''''''''''''''
import sys
sequence = sys.argv[1]
upper_sequence = sequence.upper()
print upper_sequence[:3]
print upper_sequence[3:6]
print upper_sequence[6:9]
'''''''''''''''
import sys
protein = sys.argv[1]
upper_protein = protein.upper()
print upper_protein.find("C")

