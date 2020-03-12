import tkinter as tkr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #imbedd graph into tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #used to plot graph





countries = pd.read_csv('countries.csv')
# countries = countries_df
# print(countries.head()) 
#         country year  population
# 0  Afghanistan  1952     8425333
# 1  Afghanistan  1957     9240934
# 2  Afghanistan  1962    10267083
# 3  Afghanistan  1967    11537966
# 4  Afghanistan  1972    13079460


# SIZE IS LARGE SO  I WILL ONLY ANALYZE POPULATION GROWH FROM 1952 TO 2007
#.LOC WILL LET US ACCEESS ROWS/COLUMNS TO ANALYZE WHATEVER INFO WE WANT
countries_1952 = countries.loc[countries['year']==1952]
# print(countries_1952.head(6))
#         country  year  population
# 0   Afghanistan  1952     8425333
# 12      Albania  1952     1282697
# 24      Algeria  1952     9279525
# 36       Angola  1952     4232095
# 47    Argentina  1952    17876956
# 59    Australia  1952     8691212
countries_2007 = countries.loc[countries['year']==2007]

# print(countries_2007.head())
        # country  year  population
# 11  Afghanistan  2007    31889923
# 23      Albania  2007     3600523
# 35      Algeria  2007    33333216
# 46       Angola  2007    12420476
# 58    Argentina  2007    40301927
merged_list = countries_1952.merge(countries_2007, left_on= 'country', right_on = 'country')
# print(merged_list.head())

#       country     year_x  population_x  year_y    population_y
# 0  Afghanistan    1952       8425333    2007      31889923
# 1      Albania    1952       1282697    2007       3600523
# 2      Algeria    1952       9279525    2007      33333216
# 3       Angola    1952       4232095    2007      12420476
# 4    Argentina    1952      17876956    2007      40301927


# # GET THE DIFFERENCE/POPULATION GROWTH FROM 1952 TO 2007
merged_list['population_growth'] = merged_list['population_y'] - merged_list['population_x']
# print(merged_list.head())
#        country   year_x  population_x  year_y  population_y  population_growth
# 0  Afghanistan    1952       8425333    2007      31889923           23464590
# 1      Albania    1952       1282697    2007       3600523            2317826
# 2      Algeria    1952       9279525    2007      33333216           24053691
# 3       Angola    1952       4232095    2007      12420476            8188381
# 4    Argentina    1952      17876956    2007      40301927           22424971


#MAKE THE POPULATION DIFFIRENCE IN ORDER OF ASCENDING/DESCENDING
merged_list= merged_list.sort_values('population_growth', ascending = False).head(10)
# print(merged_list.head())

#RESET INDEX/NUMBERING 
merged_list = merged_list.reset_index()
# print(merged_list)
merged_list = merged_list.drop(['index'], axis=1)
# print(merged_list)

#NOW TO SHOW THESE INFO ON A GRAPH, USING MATPLOTLIB
#X AND Y
# ONLY TOP 10 COUNTRIES COS THERE ARE ABOUT 200 COUNTRIES HERE
names = merged_list['country']
# print(names)
# Y AXIS
line = (merged_list['population_growth'] / 10**6)
# print(line)

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

plt.bar(names,line,width=0.6, color = 'pink')
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
