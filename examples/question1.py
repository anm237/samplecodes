# Question 1 in the assignment is incomplete as the criteria for passsword is not mentioned. Hence, I have asssumed a general case wherethe password length is minimum 8, should have alphanumeric characters with upper an lowercases and atleast one special case #

import re
import logging 
def validate(s):
  logging.basicConfig(filename='passlog.log',format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s') #format of the message to be displayed in the log file
  flag = 0 
  while True:   
    if (len(s)< 8):                          #checking the length of password
        flag = 1
        break
    elif not re.search("[a-z]", s):          #checking the presence of lower cases in passowrd
        flag = 1
        break
    elif not re.search("[A-Z]", s):          #checking the presence of upper cases in passowrd
        flag = 1
        break
    elif not re.search("[0-9]", s):          #checking the presence of numbers in password
        flag = 1
        break
    elif not re.search("[!@#$^&*()=+-]", s): # checking the presence of special characters in the passowrd
        flag = 1
        break
    else: 
        flag = 0
        print("Valid") 
        break
  
  if flag ==1: 
     print("Invalid") 
     logging.warning("Invalid ")             #if invalid, the warning message to be displayed in the log file
    

def main():
   s=input("enter the password : ")
   validate(s)                               #calling the validate function

if __name__=="__main__":                     #calling the main function
   main()
   
