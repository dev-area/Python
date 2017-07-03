# Python 2 version

for line in open('messier.txt'):
    if not line: break
    if line.startswith('M'):
        # Slice each field
        Mnum = line[:6].rstrip()
        Name = line[6:40].rstrip()
        if not Name: Name = 'no name'
        Type = line[40:64].rstrip()
        Cons = line[64:].rstrip()

        print "|"+Mnum+"|"+Name+"|"+Type+"|"+Cons+"|" 
        

