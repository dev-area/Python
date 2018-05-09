
def fn():
    print("start")
    try:
        print("start try block")
        f = open("file1")
        print("end try block")
    except Exception,errobj:
        print("other error " , errobj.strerror)
    else:
        print("else")
    finally:
        print("finally")

fn()
print("end")
