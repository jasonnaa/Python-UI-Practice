import customtkinter

# Assuming customtkinter provides a method to set appearance mode
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("500x350")

def switch_event():
    global switch_var
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(master=frame, text="Switch Appearance Mode", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
switch.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

