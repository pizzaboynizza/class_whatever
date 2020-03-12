import tkinter as tkr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #imbedd graph into tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #used to plot graph





countries = pd.read_csv('countries.csv')
# countries = countries_df
# print(countries.head(20))

countries_1952 = countries.loc[countries['year']==1952]
# print(countries_1952.head(6))
countries_2007 = countries.loc[countries['year']==2007]
#print(countries_2007.head())
merged_list = countries_1952.merge(countries_2007, left_on= 'country', right_on = 'country')
# print(merged_list.head(10))



#TO CLEAN UP OUR DATA, ADD YEAR TO POPULATION, FIRST DELETE YEAR AND ADD TO POPULATION RESPECTIVELY
merged_list.drop(['year_x', 'year_y'], axis=1)
# print(merged_list.head())

#MERGE YEAR WITH POPULATION
# drop_years.rename(columns = {'population_x' : 'population_1952', 'population_y' : 'population_2007'}, inplace =True)
# print(drop_years.head())


# # GET THE DIFFERENCE/POPULATION GROWTH FROM 1952 TO 2007


merged_list['population_growth'] = merged_list['population_y'] - merged_list['population_x']
# print(drop_years.head())




#MAKE THE POPULATION DIFFIRENCE IN ORDER OF ASCENDING/DESCENDING
merged_list= merged_list.sort_values('population_growth', ascending = False).head(10)
# print(population_dataframe.head())

#RESET INDEX/NUMBERING
merged_list = merged_list.reset_index()
merged_list = merged_list.drop(['index'], axis=1)
# print(merged_list)


#X AND Y

names = ['China','India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh','Nigeria','Mexico', 'Phillippines']
line = (merged_list['population_growth'] / 10**6)


window = tkr.Tk() #Creating the tkinter window##
#Editing tkinter window
window.title("Poulation Growth Graph") # window name
window.geometry('200x300') #window dimension
"""CREATE VERT SCROLL BAR"""
SBar = tkr.Scrollbar(window) #linked to window
SBar.pack(side=tkr.RIGHT, fill="y") # packed into window to the right side and fill from top to bottom

"""CREATE HORIZONTAL SCROLL BAR"""
SBar2 = tkr.Scrollbar(window, orient = tkr.HORIZONTAL) #linked to window
SBar2.pack(side=tkr.BOTTOM, fill="x") # packed into window to the right side and fill from top to bottom



# """Create Text Box"""
# TxtBox = tkr.Text(window,height = 500, width = 350, yscrollcommand = SBar.set) # link vert scrollbar to txtbox
# TxtBox.pack(expand=0, fill= tkr.BOTH) #Pack bar into window and fill any space not taken by scrollbar

# """Insert Text Into Textbox"""
# TxtBox.insert(tkr.END,names) #
# TxtBox.insert(tkr.END,line)

# """Link Scrollbar to Textbox"""
# SBar.config(command=TxtBox.yview) #link scrollbar to textbook
# SBar.config(command=TxtBox.xview)


# #BAR CHART
fig = plt.figure(figsize=(10,10))

plt.bar(names,line,width=0.6)
plt.xlabel('Countries')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries with the largest population from 1952 - 2007')
plt.xticks(rotation=45)

for x,y in zip(names,line):
    
    label = "{:.2f}".format(y)

    plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10), ha= 'center')

# plt.show()
"""LOADING GRAPH INTO TKINTER"""
chart = FigureCanvasTkAgg(fig,window) #fingurecanvas used to imbedd graph(fig) into tkinter(window)
chart.get_tk_widget().pack() #used to show the imbedded chart in tkinter
tkr.mainloop() # start and end of Tkinter GUI
