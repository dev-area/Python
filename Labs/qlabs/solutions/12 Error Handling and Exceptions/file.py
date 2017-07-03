#!/usr/bin/python
# Python 2 version
# Error handling extension
import os.path
import struct

class File(object):
    def __init__(self,filename):
        self._filename = filename
        self._error = False
        
        # If the file does not exist, create it
        if not os.path.isfile(filename):
            try:
                open(filename,'w')
            except IOError as err:
                self._error = err.args
            
    @property
    def size(self):
        if self._error:
            return None
        else:
            return os.path.getsize(self._filename)
     
    @property
    def error(self):
        return self._error
    
# Text file
class TextFile(File):
    @property
    def contents(self):
        """ Return the contents of the file """
        return open(self._filename,'rt').read()
    
    @contents.setter
    def contents(self,value):
        """ Append to the file """
        if not value.endswith("\n"):
            value += "\n";
        open(self._filename,'at').write(value)

# Binary file
class BinFile(File):
    @property
    def contents(self):
        """ Return the contents of the file """
        value = open(self._filename,'rb').read()
        return value
    
    @contents.setter
    def contents(self,value):
        """ Append to the file """
        if isinstance(value,int):
            out = struct.pack('i',value)
            open(self._filename,'ab').write(out)
        else:
            open(self._filename,'ab').write(value)
        
        
if __name__ == '__main__':
    import sys

    # Test constructor error handling
    if not os.path.isdir:
        os.mkdir('Dummy')

    dummy = TextFile('Dummy')
    print "Size of Dummy:",dummy.size 
    
    if dummy.error:
        print >> sys.stderr,"Dummy error:",dummy.error
    else:
        print >> sys.stderr,"No error detected!"
    