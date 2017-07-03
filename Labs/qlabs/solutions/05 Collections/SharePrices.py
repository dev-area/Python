# SharePrices.py for QAPYTH2
# CBD October 2011
import time
import random

SharePrices = {'Global Motors':50,
               'Big Blue Inc.':50,
               'Gates Software':50,
               'Banana Computers':50}

# Updates stock prices with random price changes

while True:

    for key,sp in SharePrices.items():
        SharePrices[key] = max(1.0,
                           sp * ( 1 + ((random.random() - 
                           0.5)/0.5) * 0.05))
        print("{:<18s} ${:05.2f}".
              format(key,SharePrices[key]))          
            
    print 

    time.sleep( 2 )
            
 