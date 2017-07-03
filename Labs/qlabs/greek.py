# Python 2 version

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Sigma final','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

#Format required:
#    The hex value of the character
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character

pos = 0x03B1         
for cname in greek:
    try:
        char = unichr(pos)
        pos += 1 
        print cname,":",char   # TODO: replace this statement
    except UnicodeEncodeError as err:
        print  cname, 'unknown'
