class Country(object):

    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    # Insert your code here
        
    def __init__(self, row):
        self.__attr = row.split(',')
            
