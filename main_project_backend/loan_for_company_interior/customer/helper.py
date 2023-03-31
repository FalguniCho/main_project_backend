from twilio.rest import Client 
from django.conf import settings



account_sid =settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
mob = settings.TWILIO_PHONE_NUMBER
client = Client(account_sid, auth_token) 

def send_message(body,to):
    message = client.messages.create(   
                              body = body,
                              from_ = mob,     
                              to = to
                          ) 
 
    print(message.sid)



