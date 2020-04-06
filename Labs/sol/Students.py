
class Student(object):
    def __init__(self,i=0,n="avi",c="haifa"):
        self.__id = i
        self.__name = n
        self.__city = c
    def getid(self):
        return self.__id
    def setid(self,i):
        self.__id = i
    def getname(self):
        return self.__name
    def setname(self,n):
        self.__name = n
    def getcity(self):
        return self.__city
    def setcity(self,c):
        self.__city = c
    def __str__(self):
        return "Student id:" + str(self.__id) + " name:" + str(self.__name) + " city:" + str(self.__city)
    
class UStudent(Student):
    def __init__(self,i=0,n="avi",c="haifa",p=0,st=0):
        super().__init__(i,n,c)
        self.__points = p
        self.__status = st
    def getpoints(self):
        return self.__points
    def setpoints(self,p):
        self.__points = p
    def getstatus(self):
        return self.__status
    def setstatus(self,s):
        self.__status = s
    def __str__(self):
        return super().__str__() + " points:" + str(self.__points) + " status:" + str(self.__status)
    
    
class GStudent(Student):
    def __init__(self,i=0,n="avi",c="haifa",pr="",sup=""):
        super().__init__(i,n,c)
        self.__project = pr
        self.__superv = sup
    def getproject(self):
        return self.__project
    def setproject(self,p):
        self.__project = p
    def getsuperv(self):
        return self.__superv
    def setsuperv(self,s):
        self.__superv = s
    def __str__(self):
        return super().__str__() + " project:" + str(self.__project) + " superv:" + str(self.__superv)


class StudentException(Exception):
    pass



class StudentList(object):
    def __init__(self):
        self.__students = []
    def __len__(self):
        return len(self.__students)
    def __getitem__(self,key):
        return self.__students[key]
    def __setitem__(self,key,value):
         self.__students[key] = value
    def __iter__(self):
        for a in self.__students:
            yield a
    def add(self,st):
        if not isinstance(st,Student):
            raise StudentException()    
        self.__students.append(st)



sl = StudentList()

s1 = Student()
s2 = GStudent()
s3 = UStudent()

sl.add(s1)
sl.add(s2)
sl.add(s3)

print(sl[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
