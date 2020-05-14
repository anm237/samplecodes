def freq(str): 
    str=open("/home/akash/Desktop/quantiphi_assignment/input.txt","r").read()  #read ghe input text file and convert it to string
    str = str.split()        						       #convert the string to list
    str1 = []             						       #initialize an empty string
  
    
    for i in str:  							       #start filling the empty string           				
       if i not in str1:                                                      
            str1.append(i)                                                                                                        
            str1.sort()                                                        #sort the string in alphanumeric order
              
    for i in range(0, len(str1)):  
            print(( str1[i], str.count(str1[i])),file=open("output.txt","a"))
 
def main(): 
    freq(str)                                                                  #calling the function
  
if __name__=="__main__": 
    main()                                                                     #calling the main function                        
