
def f2(a,b):
    if a>0:
        raise ValueError("Error in f2")
    return a+b

def f1():
    try:
        print("start try block")
        s=f2(10,20)
        print("end try block")
    finally:
        print("finally f1")
#    except Exception as ex:
#        print("Exception in f1",ex)



print("start")
try:
    f1()
except Exception:
    print("error")
print("end")
