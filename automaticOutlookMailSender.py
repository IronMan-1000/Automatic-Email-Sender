import win32com.client as client

outlook = client.Dispatch('Outlook.Application')

message = outlook.CreateItem(0) 
message.Display()
message.To = 'Sagnik1508@outlook.com'
message.CC = 'Sagnik1508@outlook.com'
message.BCC = 'Sagnik1508@outlook.com'

message.Subject = 'AutoMated Message'
message.Body = 'Sagnik Biswas is offline now. He will get back to you shortly. Thank you For your patiences. Regards, Jarvis(Sagnik Bot)'

message.Save() 
message.Send() 

