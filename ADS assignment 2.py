# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:11:50 2022

@author: Aselebe Michael
"""


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns



url = "https://api.worldbank.org/v2/en/topic/19?downloadformat=excel"
local_url = "C:\\Users\\USER\\Downloads\\record.xls"

"""
This Function is calling the worldbank URL and using the panda module and also 
transposing it

"""
def Read_data(filename):
    load_data=pd.read_excel(filename)
    return  load_data, load_data.transpose()



data = Read_data(url)

indicators = data[0]["Unnamed: 2"]

print(indicators)



def Agric_foresty_fishing(filename):
   """Function for Agriculture, forestry, and fishing, value added (% of GDP)"""
    
   indicator_payload = data[0][indicators == "Agriculture, forestry, and fishing, value added (% of GDP)"]
   
   #Re-assign indicator_payload
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin(["Canada","United Arab Emirates", "China","United Kingdom","Italy", "Japan", "Nigeria", "Indonesia" "South africa", "Austrialia","Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,'2001':year2001, '2006':year2006, '2011':year2011, '2016':year2016}, index = countries)
   
   dataFrame.plot.bar(rot=45, title="Agriculture, forestry, and fishing, value added (% of GDP)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="Agriculture, forestry, and fishing, value added (% of GDP)")
   
   plt.xlabel("Country Name")
   plt.show()
   

Agric_foresty_fishing(url)




def Electricity(filename):
   """Function for Electricity production from renewable sources, excluding hydroelectric (kWh)"""
    
   indicator_payload = data[0][indicators == "Electricity production from renewable sources, excluding hydroelectric (kWh)"]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin(["Canada","United Arab Emirates", "China","United Kingdom","Italy", "Japan", "Nigeria", "Indonesia" "South africa", "Austrialia","Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,'2001':year2001, '2006':year2006, '2011':year2011, '2016':year2016}, index = countries)
   
   dataFrame.plot.bar(rot=45, title="Electricity production from renewable sources, excluding hydroelectric (kWh)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="Electricity production from renewable sources, excluding hydroelectric (kWh)")
   plt.xlabel("Country Name")
   plt.show()
   

Electricity(url)

def Cereal_yield(filename):
   indicator_payload = data[0][indicators == "Cereal yield (kg per hectare)"]
   
   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin(["Canada","United Arab Emirates", "China","United Kingdom","Italy", "Japan", "Nigeria", "Indonesia" "South africa", "Austrialia","Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,'2001':year2001, '2006':year2006, '2011':year2011, '2016':year2016}, index = countries)
   
   dataFrame.plot.bar(rot=45, title="Cereal yield (kg per hectare)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="Cereal yield (kg per hectare)")
   plt.xlabel("Country Name")
   plt.show()
   

Cereal_yield(url)






