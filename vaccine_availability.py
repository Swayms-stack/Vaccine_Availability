"""
python vaccine_availability.py
"""

# standard imports
import requests
import datetime
import json
import pandas as pd
import smtplib

def logger(line):
    with open('log.txt','a+') as f:
        f.write(line+"\n")
        
"""
To get the state code
for state_code in range(1,40):
    # print("State code: ", state_code)
    logger("State code: "+ str(state_code))
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code))
    json_data = json.loads(response.text)
    for i in json_data["districts"]:
        # print(i["district_id"],'\t', i["district_name"])
        logger(str(i["district_id"])+'\t'+str(i["district_name"]))
    # print("\n")
    logger("\n")
"""

DIST_ID = 446
# Print available centre description (y/n)?
print_flag = 'y'

numdays = 20
age = 19
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 2))
        if resp_json["centers"]:
            # print("Available on: {}".format(INP_DATE))
            logger("Available on: {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            logger("\t" +str(center["name"]))
                            logger("\t" +str(center["block_name"]))
                            logger("\t Price: " + str(center["fee_type"]))
                            logger("\t Available Capacity: " + str(session["available_capacity"]))
                            """
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            """
                            if(session["vaccine"] != ''):
                                logger("\t Vaccine: " + str(session["vaccine"]))
                            # print("\n\n")
                            logger("\n\n")
                            
            
                
        else:
            # print("No available slots on {}".format(INP_DATE))
            logger("No available slots on {}".format(INP_DATE))

def send_mail(self):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pythonhai.000@gmail.com', 'machinelearning@#$000')

    subject = 'VACCINE NOTIFICATION'

    body = 'XXX'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Coronavirus',
        'swaymsdennings@gmail.com',
        msg
    )
    print('Email has been sent !')

    server.quit()
            