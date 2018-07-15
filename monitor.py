import struct
import time
import curses
###############################################
# Project from SecureTea (OWASP)
###############################################

# If it is not already installed, please download & install the twitter package from
# https://pypi.python.org/pypi/twitter
from twitter import *

###############################################
# Twitter API and ACCESS TOKEN NEEDED
###############################################
API_KEY = 'API_KEY'
API_SECRET = 'API_SECRET'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
twitter_username = 'twitter_username'

localtime = time.asctime(time.localtime(time.time()))
auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth=auth)
welcome_msg = "\nWelcome to Py system ..!! Initializing System @ " + localtime
print (welcome_msg)
twitter.direct_messages.new(user=twitter_username, text=welcome_msg)

def main(win):
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:          
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           out2Twi = "Detected key: " + str(key)
           twitter.direct_messages.new(user=twitter_username, text=out2Twi)
           time.sleep(10)
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass     

### Detect KeyPressed event 
curses.wrapper(main)

print ("End of program")