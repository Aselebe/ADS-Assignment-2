# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:52:53 2022

@author: haselebe
"""

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import math



url = "https://api.worldbank.org/v2/en/topic/19?downloadformat=excel"


"""
This Function is calling the worldbank URL and using the panda module and also 
transposing it

"""
def Read_data(filename):
    load_data=pd.read_excel(filename)
    return  load_data, load_data.transpose()



data = Read_data(url)

indicators = data[0]["Unnamed: 2"]



def Agric_foresty_fishing(filename):
   """Function for Agriculture, forestry, and fishing, 
   value added (% of GDP)"""
    
   indicator_payload = data[0][indicators == "Agriculture, forestry, and fishing, value added (% of GDP)"]
   
   #Re-assign indicator_payload
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin(["Canada",
                        "United Arab Emirates", "China","United Kingdom",
                        "Italy", "Japan", "Nigeria", "Indonesia" ,
                        "South africa", "Austrialia","Afghanistan" ,
                        "Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', '2011',
                                    '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,
                             '2001':year2001, '2006':year2006, 
                             '2011':year2011, '2016':year2016},
                            index = countries)
   
   dataFrame.plot.bar(rot=85, title="Agriculture, forestry, and fishing, value added (% of GDP)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                              title="Agriculture, forestry, and fishing, value added (% of GDP)")
   
   plt.xlabel("Country Name")
   plt.show()
   

Agric_foresty_fishing(url)




def Electricity(filename):
   """Function for Electricity production from renewable
   sources, excluding hydroelectric (kWh)"""
    
   indicator_payload = data[0][indicators == "Electricity production from renewable sources, excluding hydroelectric (kWh)"]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin(["Canada",
                    "United Arab Emirates", "China","United Kingdom","Italy", 
                    "Japan", "Nigeria", "Indonesia" "South africa", 
                    "Austrialia","Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', '2011',
                                    '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,'2001':year2001,
                             '2006':year2006, '2011':year2011, 
                             '2016':year2016}, index = countries)
   
   dataFrame.plot.bar(rot=85, title="Electricity production from renewable sources, excluding hydroelectric (kWh)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                              title="Electricity production from renewable sources, excluding hydroelectric (kWh)")
   plt.xlabel("Country Name")
   plt.show()
   

Electricity(url)


def Cereal_yield(filename):
   indicator_payload = data[0][indicators == "Cereal yield (kg per hectare)"]
   
   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin
                                    (["Canada","United Arab Emirates", 
                                      "China","United Kingdom","Italy", 
                                      "Japan", "Nigeria", "Indonesia", 
                                      "South africa", "Austrialia",
                                      "Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', 
                                    '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,
                             '2001':year2001, '2006':year2006, 
                             '2011':year2011, '2016':year2016}, 
                            index = countries)
   
   dataFrame.plot.bar(rot=85, title="Cereal yield (kg per hectare)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                              title="Cereal yield (kg per hectare)")
   plt.xlabel("Country Name")
   plt.show()
   

Cereal_yield(url)



"""
Defining function for CO2 emissions from liquid fuel consumption (kt)

"""
def cotwo_emission(filename):
   indicator_payload = data[0][indicators == 
                              "CO2 emissions from liquid fuel consumption (kt)"]
   
   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin
                                    (["Canada","United Arab Emirates",
                                      "China","United Kingdom","Italy", 
                                      "Japan", "Nigeria", "Indonesia" ,
                                      "South africa", "Austrialia",
                                      "Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006',
                                    '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,
                             '2001':year2001, '2006':year2006, 
                             '2011':year2011, '2016':year2016}, 
                            index = countries)
   
   dataFrame.plot.bar(rot=75, title=
                      "CO2 emissions from liquid fuel consumption (kt)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                    title="CO2 emissions from liquid fuel consumption (kt)")
   plt.xlabel("Country Name")
   plt.show()
   

cotwo_emission(url)


def urban_population(filename):
   """Defining function for Urban population indicator"""
    
   indicator_payload = data[0][indicators == "Urban population"]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin
                    (["Canada","United Arab Emirates", "China",
                      "United Kingdom","Italy", "Japan", "Nigeria", 
                      "Indonesia", "South africa", "Austrialia","Afghanistan" 
                      ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', 
                                    '2006', '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,
                             '2001':year2001, '2006':year2006, 
                             '2011':year2011, '2016':year2016}, 
                            index = countries)
   
   dataFrame.plot.bar(rot=75, title="Urban population")
   
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                              title="Urban population")
   plt.xlabel("Country Name")
   plt.show()
   

urban_population(url)


def agricultural_land(filename):
   """Defining function for Agritulture indicator"""
    
   indicator_payload = data[0][indicators == "Agricultural land (sq. km)"]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin
                                    (["Canada","United Arab Emirates",
                                      "China","United Kingdom","Italy", 
                                      "Japan", "Nigeria", "Indonesia" ,
                                      "South africa", "Austrialia",
                                      "Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006', 
                                    '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year1996 = [value for value in records.loc[:, '1996']]
   year2001 = [value for value in records.loc[:, '2001']]
   year2006 = [value for value in records.loc[:, '2006']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2016 = [value for value in records.loc[:, '2016']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'1996':year1996,
                             '2001':year2001, '2006':year2006, 
                             '2011':year2011, '2016':year2016},
                            index = countries)
   
   dataFrame.plot.bar(rot=75, title="Agricultural land (sq. km)")
   dataFrame.transpose().plot(rot=45,linestyle='dashed', 
                              title="Agricultural land (sq. km)")
   plt.xlabel("Country Name")
   plt.show()
   

agricultural_land(url)



def urban_population_table_data(filename):
   """Defining function for Urban population indicator"""
    
   indicator_payload = data[0][indicators == "Urban population"]   

   #Get Countries
   country_df = indicator_payload.iloc[:,:]

   #filtered to show only specific country
   filtered_country_df = country_df[country_df['Data Source'].isin
                                    (["Canada","United Arab Emirates", 
                                      "China","United Kingdom","Italy",
                                      "Japan", "Nigeria", "Indonesia" ,
                                      "South africa", "Austrialia",
                                      "Afghanistan" ,"Albania"])]
   country_column = filtered_country_df.loc[:,'Data Source']
   countries = [country for country in country_column]

   #Select years
   year_payload = filtered_country_df.iloc[:,[36,41,45,50,55,60,65]]
   
   records = year_payload.set_axis(['1991','1996','2001', '2006',
                                    '2011', '2016','2021'], axis=1)
   
   year1991 = [value for value in records.loc[:, '1991']]
   year2011 = [value for value in records.loc[:, '2011']]
   year2021 = [value for value in records.loc[:, '2021']]
   
   dataFrame = pd.DataFrame({'1991':year1991,'2011':year2011, 
                             '2021':year2021}, index = countries)
   dataFrame = dataFrame.rename_axis('Country').reset_index()
   try:
       dataFrame.to_excel('urban_pop_table.xlsx',index=False)
   except ModuleNotFoundError:
       print('Install openpyxl or the missing module')
   except:
       print("Something went wrong")
   else:
       print('Saved to urban_pop_table.xlsx')
           
   
urban_population_table_data(url)



heat_map=data[1]


data[1].to_csv("data transpose.csv")
data[0].to_csv("data.csv")

x = (["CO2 liquid","CO2 solid",
                                                "Urban",
                                                "Population","Arable",
                                                "Agricultural"])    
y =(["CO2 liquid","CO2 solid",
                                                "Urban population",
                                                "Population","Arable",
                                                "Agricultural"])


heatmap_nigeria = heat_map.iloc[[4,14,24,34,44,54,64],
                                [13266, 13261 ,13224,13228,13297,13298 ]]



heatmap_nigeria=heatmap_nigeria.fillna(0)

heatmap_nigeria=heatmap_nigeria.set_axis(["CO2 liquid ","CO2 solid ",
                                                "Urban",
                                                "Population",
                                                "Arable","Agricultural"],
                                                 axis=1,
                                                 inplace=False)

                

print(heatmap_nigeria)

heatmap_nigeria=heatmap_nigeria.corr()

plt.imshow(heatmap_nigeria,cmap='coolwarm', interpolation="none")
plt.colorbar()

plt.xticks(range(len(heatmap_nigeria)), heatmap_nigeria.columns, rotation=90)
plt.yticks(range(len(heatmap_nigeria)),heatmap_nigeria.columns)

labels=heatmap_nigeria.values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(x,y, '{:.2f}'.format(labels[y,x]), ha='center', 
                 va='center', color='black')
        plt.title("Nigeria")
           




"""United Kingdom Heatmap """


heatmap_United = heat_map.iloc[[4,14,24,34,44,54,64],[6219, 6203,6212,6229,6156,6230 ]]



heatmap_United=heatmap_United.fillna(0)

heatmap_United=heatmap_United.set_axis(["CO2 liquid ","CO2 solid ",
                                                "Urban",
                                                "Population",
                                                "Arable","Agricultural"],axis=1,
                                                 inplace=False)
heatmap_United=heatmap_United.corr()

plt.imshow(heatmap_United,cmap='coolwarm', interpolation="none")
plt.colorbar()

plt.xticks(range(len(heatmap_United)), heatmap_United.columns, rotation=90)
plt.yticks(range(len(heatmap_United)),heatmap_United.columns)

label=heatmap_United.values
for b in range(label.shape[0]):
    for a in range(label.shape[1]):
        plt.text(a,b, '{:.2f}'.format(label[b,a]), ha='center', va='center', color='black')
        plt.title("United Kingdom")
        
        