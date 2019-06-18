
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup (7,gpio.IN)# switch1
gpio.setup (8,gpio.IN)# switch2
gpio.setup (23,gpio.OUT)# green
gpio.setup (24,gpio.OUT)# red
gpio.setup (25,gpio.OUT)# white

while True:

    switch = gpio.input(7)
    switch1 = gpio.input(8)

    print ("switch stautus:",str(switch))
    print ("switch1 status:",str(switch1))

    # assume that if switch is pressed then its status is 0
        
    if (switch == 0):
        gpio.output(23,1)
        print ("Green LED is ON")
        gpio.output(24,0)
        #print ("Red LED is OFF")
        gpio.output(25,0)
        #print ("White LED is OFF")
        time.sleep(1)

    elif (switch1 == 0):
        gpio.output(23,0)
        #print ("Green LED is OFF")
        gpio.output(24,1)
        print ("Red LED is ON")
        gpio.output(25,0)
        #print ("White LED is OFF")
        time.sleep(1)

    else:
        gpio.output(23,0)
        #print ("Green LED is OFF")
        gpio.output(24,0)
        #print ("Red LED is OFF")
        gpio.output(25,1)
        print ("White LED is ON")
        time.sleep(1)
 
        
        
