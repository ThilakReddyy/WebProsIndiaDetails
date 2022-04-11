from bs4 import BeautifulSoup
import requests

def validate(roll,passwod,url):
    
    response = requests.request("POST", url)
    soup=BeautifulSoup(response.content,"html.parser")
    soup=soup.body
    viewstate=soup.find('input', {'id': '__VIEWSTATE'}).get('value')
    viewstategenerator=soup.find('input', {'id': '__VIEWSTATEGENERATOR'}).get('value')
    eventvalidation=soup.find('input', {'id': '__EVENTVALIDATION'}).get('value')
    eventvalidation=requests.utils.quote(eventvalidation)
    payload='__VIEWSTATE='+viewstate+'&__VIEWSTATEGENERATOR='+viewstategenerator+'&__EVENTVALIDATION='+eventvalidation+'&txtId1=&txtPwd1=&txtId2='+roll+'&txtPwd2='+passwod+'&imgBtn2.x=25&imgBtn2.y=11&txtId3=&txtPwd3='
    
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36', 
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if('Hi...' in response.text):
        return True
    return False