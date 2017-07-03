import copy 

class Country:
    
    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    # Insert your code here
    # 1a) Implement a constructor    
    def __init__(self, row):
        self.__attr = row.split(',')
        
        # 1e) Added to support + and -
        self.__attr[Country.index['population']] = \
            int(self.__attr[Country.index['population']])
            
    # 1b) Implement a print method        
    def printit(self):
        print self.__attr[Country.index['name']] 
        return self.name
        
    # 1c) Overloaded stringification
    def __str__(self):
        #return self.__attr[Country.index['name']]
        # 1g) Formating the output
        return "{0:<32} {1:>010}".format(self.name, self.population)
        
    # Getter methods
    # 1d) Implement a getter method for country name

    def name_get(self):
        return self.__attr[Country.index['name']]
    
    name = property(name_get)
    
    def population_get(self):
        return int(self.__attr[Country.index['population']])
    
    population = property(population_get)
    
    # 1e) Overloaded + and -
    def __add__(self,amount):
        retn = copy.deepcopy(self)
        retn.__attr[Country.index['population']] += amount
        return retn
        
    def __sub__(self,amount):
        retn = copy.deepcopy(self)
        retn.__attr[Country.index['population']] -= amount
        return retn
        
    # If time allows:
    # 1f)  Overloaded == (for index search)
    def __eq__(self,key):
        return (key == self.name)