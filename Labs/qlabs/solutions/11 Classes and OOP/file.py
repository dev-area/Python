#!/usr/bin/python
# Python 2 version
import os.path
import struct

class File(object):
    def __init__(self,filename):
        self._filename = filename
        
        # If the file does not exist, create it
        if not os.path.isfile(filename): 
            open(filename,'w')
            
    @property
    def size(self):
        return os.path.getsize(self._filename)
        
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
    file1 = TextFile('file1.txt')
    file1.contents = 'hello'
    file1.contents = 'world'
    
    print file1.contents 
    print "Size of file1:",file1.size 
    
    file2 = BinFile('file2.dat')
    
    file2.contents = 42
    file2.contents = 34
    file2.contents = 'EOD'

    print file2.contents 
    print "Size of file2:",file2.size 
    