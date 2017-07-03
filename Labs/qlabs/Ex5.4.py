# Chapter 5 Exercise 4
# Python 2 version
import os

start_time = 0;
LOOP_COUNT = 200
words = []
words_dict = {}
########################################################
# TIMER FUNCTIONS
def start_timer():
    global start_time
    (utime,stime) = os.times()[0:2]
    start_time = utime+stime

def end_timer(txt):
    (utime,stime) = os.times()[0:2]
    end_time = utime+stime
    print "%-12s: %05.3f seconds" % \
          (txt,end_time-start_time)

def load_data():
    global words
    words = open('words').read().split('\n')

########################################################
### TODO: USER FUNCTIONS
# Each function should return the line number
def brute_force():
    global words
    ### TODO use a 'for' loop
            
    ### TODO return the line number        

def infunc():
    global words
    ### TODO use 'in' to test for the presence of 'Zulu' in words
    ### Return 1 if present and 0 if not

def index():
    global words
    ### TODO use the index() method and return the line number

def dictionary():
    global words_dict
    ### TODO return the value for the key

########################################################
# MAIN

load_data()

# Brute force
start_timer()
for i in range(1,LOOP_COUNT):
    line = brute_force();
    
end_timer("Brute_force")
#print "Brute_force line number:",line
line = 0

# index
start_timer()
for i in range(1,LOOP_COUNT):
    line = index();
    
end_timer("Index")
#print "Index line number:",line
line = 0

# in
start_timer()
for i in range(0,LOOP_COUNT):
    line = infunc();
    
end_timer("In")

line = 0
# Create a dictionary from the words list
i = 0
start_timer()

### TODO: Create a dictionary called words_dict


for i in range(1,LOOP_COUNT):
    line = dictionary();
    
end_timer("Dictionary")
#print "Dictionary line number:",line
line = 0
