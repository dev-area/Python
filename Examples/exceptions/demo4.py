print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except IOError as errobj:
    print("error opening file:",errobj)
else:
    print("No Exceptions")
print("end")
