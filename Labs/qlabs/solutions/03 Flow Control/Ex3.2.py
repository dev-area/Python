
pin     = '0138'
limit   = 3
counter = 0

while counter < limit:
    supplied_pin = raw_input(
                     "Please enter your PIN:")
    counter += 1
    if supplied_pin == pin:
        break


if supplied_pin != pin:
    print "You had",limit,"tries and failed!"
else:
    print "Well done, you remembered it!"
    print "... and only after",counter,"attempts"

