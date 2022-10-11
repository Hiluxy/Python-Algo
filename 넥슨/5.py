#통과

import requests
import json

# response=requests.get('https://jsonmock.hackerrank.com/api/countries?name=Oceania')
# r_dict=json.loads(response.text)
# print(r_dict['data'][0]['callingCodes'][0]) #93

def getPhoneNumbers(country, phoneNumber):
    url='https://jsonmock.hackerrank.com/api/countries?name='
    response=requests.get(url+country)
    r_dict=json.loads(response.text)
    if len(r_dict['data'])==0:
        return -1
    else:
        strnum_list=r_dict['data'][0]['callingCodes']
        strnum=max(strnum_list)
        return '+'+strnum+' '+ phoneNumber

if __name__ == '__main__':
    print(getPhoneNumbers('Afghanistan','656445445'))#+93 656445445
    print(getPhoneNumbers('Puerto Rico','656445445'))#+1939 656445445
    print(getPhoneNumbers('Oceania','987574876'))#+1939 656445445
