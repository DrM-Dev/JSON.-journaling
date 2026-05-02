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
