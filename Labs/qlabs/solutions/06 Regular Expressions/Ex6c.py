# Exercise 3c, string formatting and regular expressions
# Additonal postcode validation
import re

# Part c
valid_dict = {}
valid = open('validpc.txt').read().splitlines()
for txt in valid:
    line=txt.split(',')
    valid_dict[line[0]] = line[1]
valid=None
# end of valid_dict initialisation

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid   = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file
    
    # Ignore empty lines
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces
    postcode = re.sub('[ \t\n]', '', postcode)
    
    # TODO (a): Convert to uppercase  
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters
    postcode = re.sub('([0-9][A-Z]{2})$', r' \1', postcode)
    
    # Print the reformatted postcode
    print postcode

    # TODO (b) Validate the postcode, returning a match object 'm'
    m = re.match(
        r"([A-Z]{1,2}[0-9]{1,2}[A-Z]?) [0-9][A-Z]{2}", 
        postcode)
    
    if m:
        valid = valid + 1
        # Part c
        area_district = m.groups()[0]

        if area_district in valid_dict:
            print postcode,"is in",valid_dict[area_district]
        else:
            print postcode,"not found"
    else:
        invalid = invalid + 1
        

infile.close()

# TODO (b) Print the valid and invalid totals
print valid, "valid codes and", invalid, "invalid codes"
