print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except IOError as errobj:
    print("error opening file:",errobj)
except (OSError,NameError):
    print("OS/Name problem")
except Exception:
    print("All other Exceptions")
print("end")
