import requests
from bs4 import BeautifulSoup
import xlwt
def getthedetails(roll,k,i,url,dictii,sheet1):
    listi=['Admission.No', 'RollNo', 'Name', 'Course', 'Branch', 'Semester', 'Gender', 'DOB', 'Nationality', 'Religion', ' Marks, %', 'Inter Marks, %', 'Entrance Type', 'EAMCET/ECET Rank', 'Seat Type', 'Caste', 'Last Studied', 'Joining Date', 'Phone.No', 'Mobile.No', 'Email', 'Bank A/C.No', 'Aadhar.No', 'Ration Card.No', 'Scholarship', 'Transport Halt', 'Father Name', 'Occupation', 'Mother Name', 'Father Mobile.No', 'Mother Mobile.No', 'Annual Income', 'Father mailid', 'Mother mailid', 'Correspondence Address', 'Permanent Address']
    url = url+"ajax/StudentProfile,App_Web_studentprofile.aspx.a2a1b31c.ashx?_method=ShowStudentProfileNew&_session=rw"
    style1 = xlwt.easyxf('font: bold off; align: wrap on, vert centre, horiz center')
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