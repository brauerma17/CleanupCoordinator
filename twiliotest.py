from twilio.rest import Client

account_sid = 'AC4d93c37484d86c0d618cba406c635a4c'
auth_token = 'a56f572258a1edf696065ed513dfb8f0'
client = Client(account_sid, auth_token)

message_body = "Join Earth's mightiest heroes. Like Kevin Bacon."
message_from = "+14704417455"
message_to = "+17704039860"

message = client.messages.create(body=message_body, from_=message_from, to=message_to)

print(message.sid)