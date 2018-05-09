import sys
from datetime import *
from calendar import *

sBirth = raw_input("Enter birthday (dd/mm/yyyy):")
try:
    (day, month, year) = sBirth.split('/')
    dBirth = date(int(year), int(month), int(day))
except ValueError:
    print >> sys.stderr,"Invalid date:",sBirth
    exit(1)
    
dToday = date.today()
diff = dToday - dBirth

diff = diff.days - leapdays(int(year),dToday.year)
years = diff / 365
print "Client is",years,"years old"

