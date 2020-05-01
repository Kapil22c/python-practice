from twilio.rest import Client
from credentials import account_sid,auth_token,my_cell,my_twilio
import django
# -*- coding: utf-8 -*-

print(django.get_version())
"""
Created on Sun Mar 29 13:26:42 2020

@author: Kapil
"""

client= Client(account_sid, auth_token)

msg=('Messege is sending.......\n' for i in range(5))

my_msg= ''.join(msg)

message= client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)



