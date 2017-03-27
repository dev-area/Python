# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 14:37:22 2014

@author: liran
"""

import numpy
import scipy.io.wavfile
# the double ** is a power operator, i.e. 2^15
convert_16_bit = float(2**15)

sample_rate, samples = scipy.io.wavfile.read(
    "a440-1second.wav")
print "Data type is:", samples.dtype

# scale to -1.0 -- 1.0
samples = samples / (convert_16_bit + 1.0)
print "Data type is now:", samples.dtype

# change the file
samples = samples * 0.25

# scale to -32768 -- 32767
samples = numpy.int16( samples * convert_16_bit )
print samples
print "Data type is now:", samples.dtype

scipy.io.wavfile.write("quieter.wav",
    sample_rate, samples)
    