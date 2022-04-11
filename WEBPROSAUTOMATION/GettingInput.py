from colorama import init
from termcolor import colored
import validation

def gettingtherollandpassword(url):
    roll=input("Enter Your Roll Number: ").upper()
    passwod=input("Enter Your password: ")
    if(validation.validate(roll,passwod,url)==False):
        print(colored("Roll No or Password is Wrong","red"))
        print(colored("Re Enter Your Credentials","red"))
        return gettingtherollandpassword()
    return roll,passwod

def Getthefromandto(lolli):
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

def gettheindividualormultiple():
    print("Enter the Required  Details")
    print("1: Individual Details")
    print("2. Multiple Details")
    Option=input()
    if(Option!="1" and Option!=2):
        print(colored("Enter the Valid Option","red"))
        return gettheindividualormultiple()
    return Option
def GettingTheRollInput():
    roll =input("Enter the To Roll Rumber: ").upper()
    if(len(roll)!=10):
        print(colored("Enter the Correct Roll Number","red"))
        return Getthefromandto()
    return roll