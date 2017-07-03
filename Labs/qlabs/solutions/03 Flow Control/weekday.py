# Python 2 version

# Code for reading in the date */
date = raw_input("Please enter date (DD/MM/YYYY): ")
d,m,y = date.split('/')
d = int(d)
m = int(m)
y = int(y)

"""
  Add Your Code Here: to adjust the values of
  d, m and y under certain circumstances

             d contains the day
             m contains the month
             y contains the year
"""
if m == 1 or m == 2:      
    m += 12
    if y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
        d -= 2
    else:
        d -= 1

z = 1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y//4 - y//100 + y//400

z %= 7

days = ["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]

print days[z]+'day' 
