from tkinter import *
from tkinter import ttk
import json

#=============
#Globals
FONT = ("Times New Roma", 10, "bold")
#
j_entry_name = ""
day = ""
month = ""
year = ""

#=============SETUP
window = Tk()
window.title("J.S.O.N  -   Journaling_Secrets_On_Names")
#
window_dim_x = 600
window_dim_y = 600
#
window.minsize(window_dim_x,window_dim_y)
window.maxsize(window_dim_x,window_dim_y)
window.config(padx=10,pady=10)

#_____________________________________________________
#widgets placement
widget_x = window_dim_x/4 - 40
widget_y = window_dim_x/4
#
widgets_displace = 40

###################### ENTRY NAME SECTION
j_entry_name_LABEL = Label(text="Enter the name of your journal entry here\n⚠️-remember it! it will be used to recall your journal", justify="left", font=FONT)
j_entry_name_LABEL.place(x=widget_x,y=widget_y)
#
j_entry_bar = Entry(width=50, font=FONT)
j_entry_bar.place(x=widget_x,y=widget_y+widgets_displace+5)
####

###################### DATE SECTION
date_LABEL = Label(text="Select Date Here:", justify="left", font=FONT)
date_LABEL.place(x=widget_x,y=widget_y+widgets_displace*2)

#--------day drop-down menu:
day_drop_menu_LABEL = Label(text="Day", font=FONT, justify="left")
day_drop_menu_LABEL.place(x=widget_x,y=widget_y+widgets_displace*2+20)
#----
days_list = [day+1 for day in range(0,30)] #list configuration
# print(days_list)#DEBUG
#PURRRFECT!
#
day_drop_menu = ttk.Combobox(window, values=[], state="readonly", width=5)
day_drop_menu['values'] = days_list #adding days_list to the values
day_drop_menu.set(days_list[0])
#
day_drop_menu.place(x=widget_x,y=widget_y+widgets_displace*2+50)

#--------month drop-down menu:
month_drop_menu_LABEL = Label(text="Month", font=FONT, justify="left")
month_drop_menu_LABEL.place(x=widget_x+widgets_displace*2,y=widget_y+widgets_displace*2+20)
#----
months_list = [month+1 for month in range(0,12)] #list configuration
# print(months_list)#DEBUG
#PURRRFECT!
#
month_drop_menu = ttk.Combobox(window, values=[], state="readonly", width=5)
month_drop_menu['values'] = months_list #adding months_list to the values
month_drop_menu.set(months_list[0])
#
month_drop_menu.place(x=widget_x+widgets_displace*2,y=widget_y+widgets_displace*2+50)

#--------year drop-down menu:
year_drop_menu_LABEL = Label(text="Year", font=FONT, justify="left")
year_drop_menu_LABEL.place(x=widget_x+widgets_displace*4,y=widget_y+widgets_displace*2+20)
#----
years_list = [year+1 for year in range(0,3000)] #list configuration
# print(years_list)#DEBUG
#PURRRFECT!
#
year_drop_menu = ttk.Combobox(window, values=[], state="readonly", width=5)
year_drop_menu['values'] = years_list #adding years_list to the values
year_drop_menu.set(years_list[0])
#
year_drop_menu.place(x=widget_x+widgets_displace*4,y=widget_y+widgets_displace*2+50)
year_drop_menu.set("2026")
####


