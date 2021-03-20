# import the time module 
import time 
  
# define the countdown function for 30 Days
def countdown(): 
    t = 30 * 24 * 60 * 60
    while t: 
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24) 
        timer = 'Days:{:02d} Hours:{:02d} Minutes:{:02d} Seconds:{:02d}'.format(days, hours, mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
countdown()
