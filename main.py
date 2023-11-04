import os
import sys

sys.path.append("<path of the file>/pwpush.py")
from pwpush import PWPUSH

pwd_obj = PWPUSH('<email ID>','<API Token>')
#Use same email id used in https://pwpush.com/
#Login/signup to https://pwpush.com/ and generate token

#to generate password URL
print(pwd_obj.generate_passoword_url('TEST MESSAGE'))

#go delete generated URL
pwd_obj.delete_password_url('<password URL>')

#to monitor URL like click count, IP deatils etc
pwd_obj.monitor_url('<password URL>')