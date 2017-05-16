import twilio

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1d706743535a8c94270b5e017a27aa21"
# Your Auth Token from twilio.com/console
auth_token  = "9a8cba237a65bb426f2c00ee97f603**"

## register phone -> message will be send to this phone with your demostic phone number generated

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+861365103****", 
    from_="185990**** ",
    body="Hello from Python!")

print(message.sid)