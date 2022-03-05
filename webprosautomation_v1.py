import os
from pickle import TRUE
import sys
import xlwt
import xlrd
import string
import requests
import subprocess
from xlutils.copy import copy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from colorama import init
from termcolor import colored
init()
def validate(roll,passwod):
    url = urlmain
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


def makedic():
    a_dic={'0'+str(i):'0'+str(i) for i in range(1,10)}
    for i in range(10,100):
        a_dic[str(i)]=str(i) 
    for letter in string.ascii_uppercase:
        for i in range(0,10):
            a_dic[letter+str(i)]=letter+str(i)
    lolli=list(a_dic.keys())
    return lolli


def gettingtherollandpassword():
    roll=input("Enter Your Roll Number: ").upper()
    passwod=input("Enter Your password: ")
    if(validate(roll,passwod)==False):
        print(colored("Roll No or Password is Wrong","red"))
        print(colored("Re Enter Your Credentials","red"))
        return gettingtherollandpassword()
    return roll,passwod

def gettingthecookies():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    ser = Service(DRIVER_PATH)
    driver=webdriver.Chrome(service=ser,options=options) #loading the chrome driver
    url=urlmain
    driver.get(url) #loading the url
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "txtId2")) )
    username = driver.find_element(By.NAME,'txtId2')
    username.send_keys(roll)
    password = driver.find_element(By.NAME,'txtPwd2')
    password.send_keys(passwod)
    driver.find_element(By.NAME,'imgBtn2').click()
    try:
        alert = Alert(driver)
        alert.accept()
    except:
        pass
    r=driver.get_cookies()
    driver.quit()
    return 'ASP.NET_SessionId='+r[1]['value']+'; frmAuth='+r[0]['value']


def getthedetails(roll,k,i):
    url = urlmain+"ajax/StudentProfile,App_Web_studentprofile.aspx.a2a1b31c.ashx?_method=ShowStudentProfileNew&_session=rw"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Cookie': k
    }
    payload = "RollNo="+roll+"\r\nisImageDisplay=false"
    response = requests.request("POST", url, headers=headers, data=payload)
    soup=BeautifulSoup(response.content,"html.parser")
    # print(soup.prettify())
    try:
        s=soup.find_all("div")[0].find_all("table")[0]
        dict={}
        pprev=""
        prev=""
        rowval=0
        guardian=False
        for tri in s:
            for tdi in tri:
                try:
                    now=tdi.contents[0]
                except:
                    now=""
                if(guardian==True):  
                    if(now=="Parent\\'s Details"):
                        guardian=False
                    else:
                        continue
                if(now=='Guardian Details'):
                    guardian=True
                if(prev==':'):
                    dict[pprev]=now
                    leni=max(len(pprev),len(now))
                    if(dictii[pprev]<leni):
                        dictii[pprev]=leni
                        sheet1.col(listi.index(pprev)).width = leni*360
                    try:
                        sheet1.write( i,listi.index(pprev),now,style1)
                    except:
                        pass
                    rowval=rowval+1
                pprev=prev
                prev=now           
    except:
        pass 

def printdone():
    print(colored('Done', 'green'))


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def Getthefromandto():
    From =input("Enter the From Roll Number: ").upper()
    To =input("Enter the To Roll Rumber: ").upper()
    if(len(From)!=10 or len(From)!=10):
        print(colored("Enter the Correct Roll Number","red"))
        return Getthefromandto()
    if(From[:8]!=To[:8]):
        print(colored("The First 8 digits of From and To should be same","red"))
        return Getthefromandto()
    firsti=lolli.index(From[8:])
    lasti=lolli.index(To[8:])
    if(firsti>=lasti):
        print(colored("The First Roll No should be lesser than the second One","red"))
        return Getthefromandto()    
    dict=lolli[firsti:lasti]
    return dict,From
    # return From,To


#PATH------------------
DRIVER_PATH=os.path.dirname(__file__)+'\chromedriver.exe'
pdf ='xlwt_example.xls'
excel_path='C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'
lolli=makedic()

urlmain="https://webprosindia.com/hitam/"
listi=['Admission.No', 'RollNo', 'Name', 'Course', 'Branch', 'Semester', 'Gender', 'DOB', 'Nationality', 'Religion', ' Marks, %', 'Inter Marks, %', 'Entrance Type', 'EAMCET/ECET Rank', 'Seat Type', 'Caste', 'Last Studied', 'Joining Date', 'Phone.No', 'Mobile.No', 'Email', 'Bank A/C.No', 'Aadhar.No', 'Ration Card.No', 'Scholarship', 'Transport Halt', 'Father Name', 'Occupation', 'Mother Name', 'Father Mobile.No', 'Mother Mobile.No', 'Annual Income', 'Father mailid', 'Mother mailid', 'Correspondence Address', 'Permanent Address']
#---------------------

#INTIALIZINNG THE WORKBOOK OR EXCEL SHEET-------------
print(colored("Intitalizing the EXCEL Sheet...","yellow"))
if os.path.exists(pdf):
  os.remove(pdf) 
wb=xlwt.Workbook()
try:
    rb = xlrd.open_workbook(pdf)
    wb = copy(rb)
    sheet1 = wb.get_sheet(0)
except:
    sheet1=wb.add_sheet('Sheet 1')
style = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
style1 = xlwt.easyxf('font: bold off; align: wrap on, vert centre, horiz center')
printdone()
#-------------------------------------------------------

#VALIDATING THE CREDENTIALS-----------------------------
print(colored("Validating the credentials...","yellow"))
roll,passwod=gettingtherollandpassword()
printdone()
#-------------------------------------------------------

#GETTING THE COOKIES------------------------------------
print(colored("Getting the Cookies...","yellow"))
k=gettingthecookies()
printdone()
#-------------------------------------------------------

#GETTING THE DETAILS-----------------------------------
print(colored("Getting the Details...","yellow"))
dict,rolli=Getthefromandto()
rolli=rolli[:8]
p=0
leng=len(dict)
dictii={}
for i in listi:
    dictii[i]=0
    sheet1.write(0,p,i,style)
    p=p+1
p=1
for i in dict:
    progress(p,leng)
    getthedetails(rolli+i,k,p)
    p=p+1
printdone()  
#-------------------------------------------------------

#Saving the Details in Excel Sheet----------------------
print(colored("Saving the details...","yellow"))
wb.save(pdf)
printdone()
print("The details have been saved in the ",pdf,"file")
try:
    subprocess.Popen(f"{excel_path} {pdf}")
except:
    pass

#------------------------------------------------------