import os
import copy
import xlwt
import xlrd
import Status
import subprocess
import GettingInput
import GettingTheDetails
import GettingTheCookies
from colorama import init
from MakingDictionary import makedic

if __name__ == "__main__":    
    #PATH------------------
    init()
    pdf ='xlwt_example.xls'
    excel_path='C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'
    urlmain="https://webprosindia.com/hitam/"
    lolli=makedic()
    listi=['Admission.No', 'RollNo', 'Name', 'Course', 'Branch', 'Semester', 'Gender', 'DOB', 'Nationality', 'Religion', ' Marks, %', 'Inter Marks, %', 'Entrance Type', 'EAMCET/ECET Rank', 'Seat Type', 'Caste', 'Last Studied', 'Joining Date', 'Phone.No', 'Mobile.No', 'Email', 'Bank A/C.No', 'Aadhar.No', 'Ration Card.No', 'Scholarship', 'Transport Halt', 'Father Name', 'Occupation', 'Mother Name', 'Father Mobile.No', 'Mother Mobile.No', 'Annual Income', 'Father mailid', 'Mother mailid', 'Correspondence Address', 'Permanent Address']
    #----------------------

    #INTIALIZINNG THE WORKBOOK OR EXCEL SHEET-------------
    Status.PrintStatus("Intitalizing the EXCEL Sheet...","yellow")
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
    Status.printdone()
    #-------------------------------------------------------

    #VALIDATING THE CREDENTIALS-----------------------------
    Status.PrintStatus("Validating the credentials...","yellow")
    roll,passwod=GettingInput.gettingtherollandpassword(urlmain)
    Status.printdone()
    #-------------------------------------------------------

    #GETTING THE COOKIES------------------------------------
    Status.PrintStatus("Getting the Cookies...","yellow")
    k=GettingTheCookies.gettingthecookies(urlmain,roll,passwod)
    Status.printdone()
    #-------------------------------------------------------
    
    #GettingIndividualMultipleDetailsInput------------------
    IndividualOrMultiple=GettingInput.gettheindividualormultiple()

    #GETTING THE DETAILS-----------------------------------
    if(IndividualOrMultiple==2):
        Status.PrintStatus("Getting the Details...","yellow")
        dict,rolli=GettingInput.Getthefromandto(lolli)
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
            Status.progress(p,leng)
            GettingTheDetails.getthedetails(rolli+i,k,p,urlmain,dictii,sheet1)
            p=p+1
        Status.printdone()  
    else: 
        Status.PrintStatus("Getting the Details...","yellow")
        rolli=GettingInput.GettingTheRollInput()
        dictii={}
        p=0
        for i in listi:
            dictii[i]=0
            sheet1.write(0,p,i,style)
            p=p+1
        GettingTheDetails.getthedetails(rolli,k,1,urlmain,dictii,sheet1)

    #-------------------------------------------------------

    #Saving the Details in Excel Sheet----------------------
    Status.PrintStatus("Saving the details...","yellow")
    wb.save(pdf)
    Status.printdone()
    print("The details have been saved in the ",pdf,"file")
    try:
        subprocess.Popen(f"{excel_path} {pdf}")
    except:
        pass
    #-------------------------------------------------------