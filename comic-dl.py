#!/usr/bin/env python3
from time import sleep

from apiclient.errors import HttpError

from gmailshell import GmailConnection

gc = GmailConnection('/home/marius/.gmailshell/')

n = 0
max = 500

while n < max:
   print('iteration {0} of {1}'.format(n+1, max))
   try:
       gc.download_comics('Label_51')    
       sleep(4)
       n += 1
   except HttpError as e:
       print('caught 429\nsleeping 20 seconds')
       sleep(20)
   except KeyError as e:
       n = max
       if e.args[0] == 'messages':
           print("No email(s) to check for attachments.")
       else:
           print('Hrm...KeyError: {0}'.format(e.args[0]))
           
