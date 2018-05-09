class Student(object):
    def __init__(self,id=0,name=''):
        self.__id = id
        self.__name = name
    def pr_student(self):
        print("id=" + str(self.__id) + " name=" + str(self.__name))
 
import pickle,gzip
 
s=Student(100,'avi')
s.pr_student();
 
outp = gzip.open('students', 'wb')
pickle.dump(s, outp)
outp.close()
 
inp = gzip.open('students', 'rb')
d = pickle.load(inp)
d.pr_student();
inp.close()
