import tkinter
from tkinter import Listbox, StringVar, PhotoImage
from PIL import Image, ImageTk

import customtkinter

import  serial
import time

arudino_port = 'COM9'
baud_rate = 9600

arduino = serial.Serial(arudino_port, baud_rate, timeout=1)
time.sleep(2)

# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("green")
dark_mode = False
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    appearance_mode = "dark" if dark_mode else "light"
    customtkinter.set_appearance_mode(appearance_mode)
    update_button_image()
def update_button_image():
    icon_path = "assets/light.png" if dark_mode else "assets/dark.png"
    pil_image = Image.open(icon_path)
    tk_image = ImageTk.PhotoImage(pil_image)
    toggle_btn.configure(image=tk_image)
    toggle_btn.image = tk_image

app = customtkinter.CTk()
app.geometry("1080x600")
app.title("Ports")

def start():
    selected_option = drop.get()
    selected_temperature = temperature_entry.get()
    print("Selected option: ", selected_option)
    print("Temperature: ", selected_temperature)

    arduino.write(selected_temperature.encode())
    # delay
    time.sleep(0.5)
    arduino_output = arduino.readline().decode().rstrip()
    print(f"Arduino: {arduino_output}")
    tempvalue.configure(text=arduino_output+" ℃")

    toast_message = f"Selected: {selected_option}\nTemperature: {selected_temperature}"
    show_toast(toast_message, duration=2)

def show_toast(message, duration):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo("Toast", message)
    root.destroy()

frame = customtkinter.CTkFrame(master=app)

label = customtkinter.CTkLabel(master=frame, text="Testing", font=("Helvetica", 30, 'bold'))
label.grid(row=0, column=1, pady=(20, 0))

label = customtkinter.CTkLabel(master=frame, text="Fluid", font=('Roboto', 25, ))
label.grid(row=1, column=0, padx=(80, 10), pady=20)

options = ["liquid 1", "liquid 2", "liquid 3", "liquid 4", "liquid 5", "liquid 6", "liquid 7", "liquid 1", "liquid 2", "liquid 3", "liquid 4", "liquid 5", "liquid 6", "liquid 7", "liquid 1", "liquid 2", "liquid 3", "liquid 4", "liquid 5", "liquid 6", "liquid 7"]
drop = customtkinter.CTkComboBox(master=frame, values=options, width=550, font=('Roboto', 14))
drop.grid(row=1, column=1, padx=(20, 20), pady=20)

btn = customtkinter.CTkButton(master=frame, text="Start", width=150, font=('Roboto', 14), fg_color="#4E7E64", hover_color="black", command=start)
btn.grid(row=1, column=2, padx=(30, 20), pady=20)

# theme toggle
image_default = Image.open("assets/dark.png")
default_image = customtkinter.CTkImage(image_default)
toggle_btn = customtkinter.CTkButton(master=frame, text="", image=default_image, fg_color='#94CDF0', command=toggle_theme, width=40, height=30)
toggle_btn.place(x=10, y=10)
update_button_image()

# temperature
temperature_label = customtkinter.CTkLabel(master=frame, text="Temperature  ℃", font=('Roboto', 14, 'bold'))
temperature_label.grid(row=2, column=0, padx=(70, 0))

temperature_entry = customtkinter.CTkEntry(master=frame, font=('calibre', 14, 'bold'), width=400)
temperature_entry.grid(row=2, column=1)

temperature_btn = customtkinter.CTkButton(master=frame, text="Stop", font=('Roboto', 14), width=150, fg_color='#FF6C5C', hover_color="black")
temperature_btn.grid(row=2, column=2, padx=(10, 0))

# innerframe1
tempframe = customtkinter.CTkFrame(master=frame, width=200, height=300)
tempframe.grid_propagate(False)

image = Image.open("assets/temperature.png")
tempimage = customtkinter.CTkImage(image, size=(50, 50))
temp_label = customtkinter.CTkLabel(master=tempframe, text="", image=tempimage)
temp_label.grid(padx=55, pady=(50, 10))

templabel = customtkinter.CTkLabel(master=tempframe, text="Temperature", font=('Roboto', 14, 'bold'))
templabel.grid(padx=55, pady=(0, 40))

tempvalue = customtkinter.CTkLabel(master=tempframe, text="100 ℃", font=('Roboto', 25, 'bold'))
tempvalue.grid(padx=55, pady=10)

tempframe.grid(pady=(80, 50), padx=(30, 0), row=3, column=0)

# inner frame2
denframe = customtkinter.CTkFrame(master=frame, width=200, height=300)
denframe.grid_propagate(False)

image = Image.open("assets/density.png")
denimage = customtkinter.CTkImage(image, size=(50,50))
den_label = customtkinter.CTkLabel(master=denframe, text="", image=denimage)
den_label.grid(padx=50, pady=(50, 10))

denlabel = customtkinter.CTkLabel(master=denframe, text="density", font=('Roboto', 14, 'bold'))
denlabel.grid(padx=50, pady=(0, 40))

value = customtkinter.CTkLabel(master=denframe, text="100 kg/m3", font=('Roboto', 25, 'bold'))
value.grid(padx=50, pady=10)

denframe.grid(pady=(80, 50), padx=(0, 0), row=3, column=1)

# innerframe3
visframe = customtkinter.CTkFrame(master=frame, width=200, height=300)
visframe.grid_propagate(False)

image = Image.open("assets/viscosity.png")
visimage = customtkinter.CTkImage(image, size=(50, 50))
vis_label = customtkinter.CTkLabel(master=visframe, image=visimage, text="")
vis_label.grid(padx=55, pady=(50, 10))

vislabel = customtkinter.CTkLabel(master=visframe, text="viscosity", font=('Roboto', 14, 'bold'))
vislabel.grid(padx=55, pady=(0, 40))

value = customtkinter.CTkLabel(master=visframe, text="100 cSt", font=('Roboto', 25, 'bold'))
value.grid(padx=55, pady=10)

visframe.grid(pady=(80, 50), padx=(0, 40), row=3, column=2)

# back button
image_btn = Image.open("assets/back.png")
back_image = customtkinter.CTkImage(image_btn, size=(25, 23))
back_btn = customtkinter.CTkButton(master=frame, text="", image=back_image, fg_color='#3BA2E3', width=55, height=35)
back_btn.place(x=980, y=545)

frame.grid(pady=10, padx=10)

app.mainloop()