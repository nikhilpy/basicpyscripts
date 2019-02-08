print ('Welcome to GST module!')
import time , sys
while True:
    print ('Please enter the amount')
    basic = input()
    if int(basic) < 0:
            print('Please enter a positive integer')
    else :    
            gst = (int(basic)*18)/100
            print ('Gst amount is : ' +str(gst))
            INCGSTPrice = (int(basic)) + (int(gst))
            print ('Total cost including GST will be : ' + str(INCGSTPrice))
         
