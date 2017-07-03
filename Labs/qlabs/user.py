from Country import Country

countries = []
# Question 1a, implement a constructor
for line in open('country.txt') :
    countries.append(Country(line))

# Question 1b, implement a print method    
#for country in countries:
    #country.printit()
    
    # Question 1c, implement string overloading
    #print country
    
    # Question 1d, implement a getter function for population
    #print country,
    #print country.population

# Question 1e, overload + and -
#print "Before:",countries[20].population
#countries[20] += 10
#print "After adding 10:",countries[20].population

#countries[20] = countries[20] - 3
#print "After subtracting 3:",countries[20].population

# Check if the __add__ worked
#first = countries[0]
#Neverland = first + 100
#if Neverland.population == first.population:
#    print "Your __add__ did not do a deepcopy!"
#elif Neverland.population == first.population + 100:
#    print "Congratulations, your __add__ worked!"
#else:
#    print "Your __add__ needs some attention!"
    
# If time allows:
# Question 1f, overload the == operator   
#here = countries.index('Sweden')
#sweden = countries[here]
#print (sweden)

# Question 1g, amend the __str__ to format the name and population
#sweden += 42
#print sweden
#print sweden + 4
#print sweden - 3

    


