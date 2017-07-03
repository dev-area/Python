import re

def prep_row (row):
    row = row.rstrip()
    row = re.sub(r"'",r"''",row)
    
    # Add quotes around each field
    #lrow = list((map(lambda f: "'"+f+"'", row.split(','))))
    
    lrow = []
    for field in row.split(','):
        lrow.append("'" + field + "'")
    
    return ",".join(lrow)
    
    
for row in open("country.txt"):
    print prep_row(row)

