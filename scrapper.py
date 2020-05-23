import requests
import json
import time 
from tqdm import tqdm

URL = "http://rankandfiled.com/data/identifiers?start="
NUMBER_OF_RECORDS = 13600
pbar = tqdm(total=NUMBER_OF_RECORDS)

def fetch_data(url,number_of_records):
    data = []
    i = 0
    while True:
        pbar.update(i*200/number_of_records)
        res = requests.get(url + str(i))
        if i > number_of_records :
            break
        json_data = res.json()
        
        if i == number_of_records:
            data = data + json_data['list']
        else:
            data = data + json_data['list'][:-1]

        i = i + 100
    pbar.close()
    return data

def get_exchange(code):
    exchanges = {
        'Q' : 'NASDAQ',
        'N' : 'NYSE',
        'A' : 'NYSE MKT',
        'P' : 'NYSE ARCA',
        'Z' : 'BATS',
        'BB': 'OTCBB',
        'NBB':'OTC',
        'G': 'NASDAQ',
        'S': 'NASDAQ'
    }
    return exchanges.get(code,'')

def format_data(data):
    formated_data = {}
    for count,item in enumerate(data):
        splited_item = item.split("|")
        temp_dict = {}
        temp_dict["CIK"] = splited_item[3]
        temp_dict["Name"] = splited_item[4]
        temp_dict["Ticker"] = splited_item[0]
        temp_dict["Exchange"] = get_exchange(splited_item[4])
        temp_dict["Business"] = splited_item[6]
        temp_dict["Incorporated"] = splited_item[7]
        temp_dict["Industry"] = splited_item[2]
        temp_dict["Ticker"] = splited_item[0]
        temp_dict["IRS Number"] = splited_item[5]

        formated_data[str(count)] = temp_dict
    
    return formated_data



data = fetch_data(URL,NUMBER_OF_RECORDS)

formated_data = format_data(data)

with open('data.json', 'w') as json_file:
  json.dump(formated_data, json_file)

print(str(len(formated_data)) + " Records Scrapped")
print("Records are stored in data.json file")




