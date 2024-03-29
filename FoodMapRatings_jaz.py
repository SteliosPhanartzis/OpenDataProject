
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import json
import re
import geopy
import datetime
dt = datetime.datetime.now()


# In[10]:


url = 'https://www.nycgovparks.org/bigapps/DPR_Eateries_001.json'
fvt = pd.read_json(url)
fvt.head()
length = str(len(fvt))
print('Total number of active Food Stations: '+ length)
fvt[['name','end_date','permit_number','park_id','type_name']]





# In[11]:


getName = ""
strName = str(fvt['name'])
currentDate = str(dt.date())
endDate = 1
# Checks if user input is a valid food truck
def validName(getName):
    getName = input("Enter name of Food Station: ")
    while(getName not in strName):
        getName = input('Please re-enter a valid Food Station (case-sensitive): ')    
    if (getName in strName):
        match(getName)
        return 1
#Asks user if they want to check another Food Stations     
def check():
    user = input("Check if another Food Station is valid? ")
    print('\n')
    if (user.lower() == 'yes'):
        getName = input("Enter name of Food Station: ")
        match(getName)
    elif(user.lower() == 'no'):    
        exit()
        
# matches the name with the location in the table       
def match(getName):
    for i in range (0,249):
        if(getName == fvt.iloc[i]['name']):
            print('Location in Table: [' + str(i) + "]")
            isItExpired(i)
            return i
        
        
#Checks if Food Station Permit is Expired        
def isItExpired(endDate):
    i = str(endDate)
    pn = fvt.iloc[endDate]['permit_number']
    expiration = fvt.iloc[endDate]['end_date']
    if(i < currentDate):
        print("Permit for" + getName + " expired on " + str(expiration) +". Citation needed!" )
        print("Permit Number: " + str(pn))
    elif(i > currentDate):
        print("Permit is still valid")
        check()
        

validName(getName)
#match(getName)
        
fvt_name = fvt['name']
listName = str(fvt_name)



#print(currentDate)

        


# In[30]:


#Create a new table of just the permit numbers that are expired, with location and name
extracted_data = {"Name": [fvt['name'][0:248]], 'Location': [fvt['location'][0:248]]}
df = pd.DataFrame(extracted_data, columns = ['Name', 'Location'])
df


# In[16]:


fvt

