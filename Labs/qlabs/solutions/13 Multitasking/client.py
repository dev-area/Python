import sys
import glob

if len(sys.argv) < 2:
    exit("No filename supplied\n")

argv = []
del(sys.argv[0])

if sys.platform == "win32":
    for pattern in sys.argv:
        filename = glob.glob(pattern)
        if len(filename) == 0:
            exit("Invalid filename:"+pattern)
        argv += filename
    
else:
    argv = sys.argv
    
for file in argv:
    dash = int(38 - int(len(file)/2))
    print "\n",'-' * dash, file, '-' * dash
    for line in open(file) :
        print line,
    

