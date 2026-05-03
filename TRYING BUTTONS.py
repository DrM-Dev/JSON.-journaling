import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.maxsize(300,200)
app.minsize(300,200)
#
custom_app = customtkinter.CTk()
custom_app.title("TRANSPARENT BUTTON TESTING")
custom_app.iconbitmap("images/iconbitmap.png")

# 1. Load and define the image using CTkImage
# You can set different images for light/dark mode if needed
my_image = customtkinter.CTkImage(light_image=Image.open("images/button_test_ON.png"),
                                  dark_image=Image.open("images/button_test_Clicked.png"),
                                  size=(30, 30)) # Set desired size in pixels

# 2. Create the button with the image
button = customtkinter.CTkButton(master=app,
                                 text="Click Me",
                                 image=my_image,
                                 compound="left",

                                 corner_radius=0,
                                 border_width=0,
                                 # hover = False
                                 ) # Position: left, right, top, or bottom
button.pack(pady=20, padx=20)

app.mainloop()
