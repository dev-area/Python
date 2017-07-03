class Country(object):

    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    # Insert your code here
    # 1a) Implement a constructor    
    def __init__(self, row):
        self.__attr = row.split(',')
            
    # 1b) Implement a print method        
    def printit(self):
        print self.__attr[Country.index['name']]
        
    # 1c)  Overloaded stringification
    def __str__(self):
        return self.__attr[Country.index['name']]