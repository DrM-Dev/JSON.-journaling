from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from pathlib import Path

#=============
#Globals
FONT = ("Times New Roma", 10, "bold")
#
j_entry_name = ""
day = ""
month = ""
year = ""
entry_data = ""

#=============SETUP
window = Tk()
window.title("J.S.O.N  -   Journaling_Secrets_On_Names")
#
window_dim_x = 600
window_dim_y = 600
#
window.minsize(window_dim_x,window_dim_y)
window.maxsize(window_dim_x,window_dim_y)
window.iconbitmap("images/iconbitmap.ico")
window.config(padx=10,pady=10)

#_____________________________________________________
#widgets placement
widget_x = window_dim_x/4 - 40
widget_y = window_dim_x/4 + 40
#
widgets_displace = 40

###################### LOGO-CANVAS:
main_canvas = Canvas(width=400, height=180)
main_canvas.place(x=window_dim_x/4-60,y=window_dim_y/4-150)

#adding image:
logo_file = PhotoImage(file=r"images/cover.png")
#
logo_widget = main_canvas.create_image(400/2,180/2,image = logo_file)


###################### ENTRY NAME SECTION
j_entry_name_LABEL = Label(text=">Enter the name of your journal entry here\n>You can search for the entry you saved using its name", justify="left", font=FONT)
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


###################### TEXT BOX (the meat and potatoes)
text_box_LABEL = Label(text="Write your memories here:", font=FONT, justify="left")
text_box_LABEL.place(x=widget_x,y=widget_y+widgets_displace*4+20)
#----
main_text_box = Text(width=50, height=10, font=FONT)
main_text_box.place(x=widget_x,y=widget_y+widgets_displace*5-40)


###################### SAVE-SYSTEM
#_____________________________
new_data = {
    f"Example Entry Name":{
        #
        "Day" : f"{day_drop_menu.get()}",
        "Month": f"{month_drop_menu.get()}",
        "Year": f"{year_drop_menu.get()}",
        #
        "ENTRY" : "\n"f"Entry Data"
    }
}
#---------------------------------
def save_file():
    global j_entry_name
    global day
    global month
    global year
    global entry_data
    global new_data
    ############
    j_entry_name = j_entry_bar.get()
    day = day_drop_menu.get()
    month = month_drop_menu.get()
    year = year_drop_menu.get()
    entry_data = main_text_box.get("1.0", "end-1c")
    #
    #debug:
    print(entry_data)
    #_____________________________
    new_data = {
        f"{j_entry_name}": {
            #
            "Day": f"{day}",
            "Month": f"{month}",
            "Year": f"{year}",
            #
            "ENTRY": "\n"f"{entry_data}"
        }
    }
    #_____________________________
    try:
        with open(r"data/data.json", "r") as data_file:
            updated_data = json.load(data_file)           #--> TAKING stored data
            updated_data.update(new_data)  #--> updating said data
            print("DATA GRABBED")
            #####
        with open(r"data/data.json", "w") as data_file:
            json.dump(updated_data, data_file, indent=4) #--> RE-INSERTING IT BACK to the file
            print("UPDATED")
        # DEBUG
        print("file reached")
    # -----------
    except FileNotFoundError:
        messagebox.showerror(title="DATA FOLDER MOVED!",
                             message="data folder have been moved/deleted\n follow the instructions in the text box :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        main_text_box.delete("1.0", END)
        main_text_box.insert(END, f"ERROR!⚠️\nNO DATA STORAGE FOUND!!!\n the [data] folder might be deleted/replaced"
                                  f"\n\nwe made you a new one! check it near the app"
                                  f"\nthe program will rebuild a new database as well :)")
        #+++++++++++++++++++++++++++DEBUG2
        print("file created")
        #
        with open(r"data/data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)


#-------------SAVE BUTTON
save_button = Button(text="SAVE💾", font=FONT, bg="blue", fg="white", command=save_file, width=30)
save_button.place(x=widget_x,y=widget_y+widgets_displace*5+130)
####
window.bind('<Return>', lambda event: save_button.invoke()) #activate with Return-key "Enter"


###################### SEARCH/RECOVER-SYSTEM
def recover_entry():
    requested_entry_name = j_entry_bar.get()
    # _____________________________
    try:
        if requested_entry_name == "":
            messagebox.showwarning(title="Empty Search", message="Please check the instructions\nprovided in the text box :)")
            ####
            main_text_box.delete("1.0", END)
            main_text_box.insert(END, f"ERROR!⚠️\nYou didn't enter an entry name!!"
                                      f"\n\nclick [OPEN DAIRY] to check the entries you saved!"
                                      f"\nor make a new entry name and press [SAVE]"
                                      f"\nthen look for it by name using [OPEN]")
        else:
            with open(r"data/data.json", "r") as data_file:
                recovered_data = json.load(data_file)
            #----
            main_text_box.delete("1.0",END)
            #----
            output = recovered_data[requested_entry_name]
            print(f"DEBUG DETAILS: \noutput:{output}\n{type(output)}")
            #----
            final_output = (f"Entry name: {requested_entry_name}"
                            f"\nDate: {output['Day']}/{output['Month']}/{output['Year']}"
                            f"\n\nEntry Content:\n{output["ENTRY"]}")
            print(f"\n\n\nTHIS: {final_output}")
            ####
            main_text_box.insert(END, final_output)
            ####

    # -----------
    except FileNotFoundError:
        messagebox.showerror(title="DATA FOLDER MOVED!",
                             message="data folder have been moved/deleted\n follow the instructions in the text box :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        main_text_box.delete("1.0", END)
        main_text_box.insert(END, f"ERROR!⚠️\nNO DATA STORAGE FOUND!!!\n the [data] folder might be deleted/replaced"
                                  f"\n\nwe made you a new one! check it near the app"
                                  f"\nthe program will rebuild a new database as well :)")
        #+++++++++++++++++++++++++++DEBUG2
        print("file created")
        #
        with open(r"data/data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    # -----------
    except KeyError:
        messagebox.showwarning(title="No file", message="No Entry with such name was found \n follow instructions provided in the text box! :)")
        ####
        main_text_box.delete("1.0", END)
        main_text_box.insert(END, f"️ERROR!⚠️\nthe requested entry {requested_entry_name}\nwas NOT FOUND"
                                  f"\n\nyou can write a new entry by the same name"
                                  f"\n write here then click [SAVE]"
                                  f"\n or just make sure to copy the name correctly, no extra spaces\n:)")
    # -----------

#-------------SEARCH-BUTTON
search_button = Button(text="OPEN📖", font=FONT, bg="orange", fg="black", command=recover_entry, width=11)
search_button.place(x=widget_x+255,y=widget_y+widgets_displace*5+130)





###################### LIST ALL ENTRIES STORED:
def show_storage():
    # _____________________________
    try:
        with open(r"data/data.json", "r") as data_file:
            recovered_data = json.load(data_file)
            output = recovered_data

        #----#formatting
        formatted_output = ""
        n=1
        for data_log in output:
            formatted_output += f"\n{n}-  {data_log}  |  Date {output[data_log]["Day"]}/{output[data_log]["Month"]}/{output[data_log]["Year"]}"
            n+=1
        ####
        main_text_box.delete("1.0", END)
        main_text_box.insert(END, f"Entry Names In Data:\n{formatted_output}")
        ####
        # Day
        # Month
        # Year
        # ENTRY

        # ----------------------
    except FileNotFoundError:
        messagebox.showerror(title="DATA FOLDER MOVED!",
                               message="data folder have been moved/deleted\n follow the instructions in the text box :)")
        ####
        Path("data").mkdir(exist_ok=True)
        ####
        main_text_box.delete("1.0", END)
        main_text_box.insert(END, f"ERROR!⚠️\nNO DATA STORAGE FOUND!!!\n the [data] folder might be deleted/replaced"
                                  f"\n\nwe made you a new one! check it near the app"
                                  f"\nthe program will rebuild a new database as well :)")
        #+++++++++++++++++++++++++++DEBUG2
        print("file created")
        #
        with open(r"data/data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)


#-------------LIST STORED-DATA BUTTON
show_storage_button = Button(text="Open Dairy🔍", font=FONT, bg="silver", fg="black", command=show_storage, width=43)
show_storage_button.place(x=widget_x,y=widget_y+widgets_displace*5+160)




#==============END
window.mainloop()
