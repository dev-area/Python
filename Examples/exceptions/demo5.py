
def f2():
    try:
        print("f2")
#        f = open("file1")
    except Exception as e:
        print("Exception in f2")
    else:
        print("No Exceptions")
        f = open("file1")


def f1():
    try:
        print("start try block")
        f2()
        print("end try block")
    except Exception:
        print("Exception in f1")



print("start")
f1();
print("end")
