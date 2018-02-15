#Imports Data from Food Vendor Table
#Render table
#Preview table
##
##import pip
##def install(package):
##    pkgs = ['mutagen', 'gTTS']
##    for package in pkgs:
##        try:
##            import package
##        except ImportError:
##            pip.main(['install', package])
##            import package
#Installs pandas
##if __name__ == '__main__':
##    install('pandas')
import pandas as pd

#Food Vendor Table
fv_url = 'https://data.cityofnewyork.us/resource/d9fw-zp4j.json'
#Restaurant Grade Table
rg_url = 'https://data.cityofnewyork.us/resource/xx67-kt59.json'

#Possible Links
##https://www.nycgovparks.org/bigapps/DPR_Eateries_001.json
##https://www.nycgovparks.org/bigapps/DPR_Concessions_001.json
##https://data.cityofnewyork.us/resource/czg9-hfnz.json
##https://data.cityofnewyork.us/resource/mp9e-iwqn.json
##https://data.cityofnewyork.us/resource/8iba-ij2b.json

#Load table
fv_t = pd.read_json(fv_url)
#Display rows
fv_t.head()
#Get the first row
row = fv_t.iloc[0]
#Get attributes from the first row
row['company_name']
row['address']
#Get selected columns for the selected rows
fv_t[['company_name','address','subindustry','sub_subindustry']][0:]
#Length of list
print(len(fv_t))
print(fv_t)
