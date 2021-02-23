import requests
from bs4 import BeautifulSoup
from datetime import datetime
from twilio.rest import Client
import time
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
phone_number = ""
phone_list = [""]
#DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'hh:mm:ssZ");

URLs = ["https://www.handsonphoenix.org/opportunity/a0C1J00000LMS0ZUAX", "https://www.handsonphoenix.org/opportunity/a0C1J00000LMiW7UAL"]

ms_sid = ""

#for number in phone_list:
#    message = client.messages.create(to=number, messaging_service_sid=ms_sid, body="This is a test, Let Ely know if you recieve the message. Verification word is: Cheese it")
#    print(message.sid)


while(1):
    print("retrieving page")
#    m1 = client.messages.create(to=phone_list[0], from_=phone_number, body="Retrieving Page")
#    print(m1.sid)
    for URL in URLs:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('span', class_='inline-element spots-remaining')
        date_blocks = soup.find_all('fieldset', class_='row fieldset-step')
        all_gone = True
        for block in date_blocks:
            try:
                today = datetime.now()
                date_text = block.find('input', class_='startDate').get('value')
                date_time_obj = datetime.strptime(date_text, "%Y-%m-%dT%H:%M:%SZ")
                if today.day == date_time_obj.day:
                    print("todays date has spaces, skipping")
                    continue
                #date_time_obj = datetime.fromisoformat(date_text)
                spots_text = block.find('span', class_='inline-element spots-remaining')
                spots_available = int(spots_text.decode_contents())
                if datetime.hour == 13:
                    date_pretty = f"{date_time_obj.strftime('%B %D')} at 6am"
                else:
                    date_pretty = f"{date_time_obj.strftime('%B %D')} at 11am"
                if spots_available > 0:
                    all_gone = False
                    for number in phone_list:
                        message = client.messages.create(to=number, messaging_service_sid=ms_sid, body=f"Spot found for {date_pretty}. Sign Up Fast!")
                    print(message.sid)
            except Exception as e:
                print(e)
    if all_gone:
        print("All the spots are gone")
        time.sleep(10)
    else:
        print("there are spots, spamming now")
        time.sleep(30)
#for to in phone_list:
#    for i in range(3):
#        print(f'sending message to {to}')
#        message = client.messages.create(to=to, from_=phone_number, body=f"Spot found for {date_pretty}. Sign Up Fast. I said Fast!")
#        print(message.sid)
#        time.sleep(20)
