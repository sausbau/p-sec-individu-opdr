import requests
import json
from datetime import datetime

def req(ip,user):
    res = requests.post(f'http://ip-api.com/json/{ip}').json() #with this api it wil make a request to get al information it can find of a specifick ip in this case the ip of someone who make a login attempt
    time = datetime.now()
    res['time_of_req'] = f'{time}'
    res['user'] = user

    with open("monitor.json",'r+') as file: #here it wil write to the json file all the information it got from the ip-api the time and the user that was attempt to login in
        file_data = json.load(file)
        file_data["Ip_monitored"].append(res)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.write('\n')
