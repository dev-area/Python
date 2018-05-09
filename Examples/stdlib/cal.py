import calendar
 
c=calendar.Calendar()
for n in c.itermonthdays(2016,2):
    print(n)
