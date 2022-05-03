from twilio.rest import Client 
 
account_sid = 'AC985fe0b590766b9251337decc3464ae5' 
auth_token = '467b8bbb248dbeb6c4cae6ad476133d5' 
client = Client(account_sid, auth_token) 
     
def send_msg():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Message from code',      
                                  to='whatsapp:+919176087937' 
                              ) 
     
    print(message.sid)
    
send_msg()