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

"""
Defining function for CO2 emissions from liquid fuel consumption (kt)

"""
def cotwo_emission(filename):
   indicator_payload = data[0][indicators == "CO2 emissions from liquid fuel consumption (kt)"]
   
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
   
   dataFrame.plot.bar(rot=45, title="CO2 emissions from liquid fuel consumption (kt)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="CO2 emissions from liquid fuel consumption (kt)")
   plt.xlabel("Country Name")
   plt.show()
   

cotwo_emission(url)


def urban_population(filename):
   """Defining function for Urban population indicator"""
    
   indicator_payload = data[0][indicators == "Urban population"]   

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
   
   dataFrame.plot.bar(rot=45, title="Urban population")
   
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="Urban population")
   plt.xlabel("Country Name")
   plt.show()
   

urban_population(url)


"""
Defining function for Agritulture indicator

"""
def agricultural_land(filename):
   """Defining function for Agritulture indicator"""
    
   indicator_payload = data[0][indicators == "Agricultural land (sq. km)"]   

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
   
   dataFrame.plot.bar(rot=45, title="Agricultural land (sq. km)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', title="Agricultural land (sq. km)")
   plt.xlabel("Country Name")
   plt.show()
   

agricultural_land(url)

def heatmap(filename):
   """Defining function for Agritulture indicator"""
   columns = ["Urban population growth (annual %)","CO2 emissions from liquid fuel consumption (% of total)","Electricity production from oil sources (% of total)", "Arable land (% of land area)", "Agricultural land (sq. km)", "Cereal yield (kg per hectare)"]
   indicator_payload = data[0][indicators.isin(columns)]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'] == 'China']

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,45,50,55,60,65]]
   
   records = year_payload.set_axis(columns, axis=1)
   
   year1991 = [value for value in records.loc[:, columns[0]]]
   year2001 = [value for value in records.loc[:, columns[1]]]
   year2006 = [value for value in records.loc[:, columns[2]]]
   year2011 = [value for value in records.loc[:, columns[3]]]
   year2016 = [value for value in records.loc[:, columns[4]]]
   year2021 = [value for value in records.loc[:, columns[5]]]

   try:
       dataFrame = pd.DataFrame({columns[0]:year1991,columns[1]:year2001, columns[2]:year2006, columns[3]:year2011, columns[4]:year2016, columns[5]:year2021}, index=columns)
       sns.heatmap(dataFrame, cmap = 'viridis', linewidths=0.30, annot=True)
       plt.show()
   except ValueError:
       print("Some of the indicators are invalid, print(filtered_country_df['Unnamed: 2']) to see what indicators are being returned and compare with columns")
   

heatmap(url)




#Heatmap for 

###UNITED KINGDOM


United_Kingdom=data[0].iloc[[6156,6158,6198,6212,6202],:]

print (United_Kingdom)

United_Kingdom = United_Kingdom.reset_index()
print(United_Kingdom)

United_Kingdom = United_Kingdom.set_axis(["Year","Urban population growth (annual %)",
                                      "CO2 emissions from liquid fuel consumption (% of total)",
                                      "Electricity production from oil sources (% of total)",
                                      "CO2 emissions from gaseous fuel consumption (% of total))"], axis=0)

United_Kingdom=United_Kingdom.iloc[[1,2,3,4],5:]

United_Kingdom.replace(np.nan,'',regex=True)

print(United_Kingdom)


United_Kingdom.replace(np.nan,'',regex=True)

United_Kingdom = np.random.rand(4, 4)


United_Kingdom.corr()
f, ax = plt.subplots(figsize=(9, 6))
ax = sns.heatmap(United_Kingdom, annot = True,
                 cmap = 'coolwarm', linecolor = 'black',
                 linewidths = 2, robust = True)
ax.set_title('United Kingdom')
ax.set_xlabel(["Urban population","CO2 emissions Liquid","Electricity production from oil", "CO2 emissions from gaseous"])

#ax.set_ylabel(["Urban population","CO2 emissions Liquid","Electricity production from oil", "CO2 emissions from gaseous"])
#f.savefig('My heatmap.png')
labels=(["Urban population","CO2 emissions Liquid","Electricity production from oil", "CO2 emissions from gaseous"])

#plt.xticks( labels, rotation='vertical')

#plt.show()







