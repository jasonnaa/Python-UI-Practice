import customtkinter
import hashlib
import pyodbc

h = hashlib.new("SHA256")

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("500x350")

# Establish connection to the SQL Server database
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS;"
    "Database=____;"
    "Trusted_Connection=yes;"
    "UID=____;"
    "PWD=____;"
)

def switch_event():
    global switch_var
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def register():
    global conn
    username = entry1.get()
    password = entry2.get()
    
    #passworword hashing
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Store the username and hashed password in the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    cursor.close()
    
    print("User registered successfully!")

def login():
    global conn
    username = entry1.get()
    password = entry2.get()
    
    # Hash the password for validation
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the username and hashed password match in the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password_hash))
    user = cursor.fetchone()
    cursor.close()
    
    if user:
        print("Login successful!")
    else:
        print("Invalid username or password!")

def switch_to_login():
    # Destroy the current window and create a new one for the login page
    create_login_page()
    root.destroy()

def create_login_page():
    login_root = customtkinter.CTk()
    login_root.geometry("500x350")

    frame = customtkinter.CTkFrame(master=login_root)
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

    register_button = customtkinter.CTkButton(master=frame, text="Switch to Register", command=create_register_page)
    register_button.pack(pady=12, padx=10)

    login_root.mainloop()

def create_register_page():
    # Destroy the current window and create a new one for the register page
    create_register_page()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(master=frame, text="Switch Appearance Mode", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
switch.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Register System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

register_button = customtkinter.CTkButton(master=frame, text="Register", command=register)
register_button.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(master=frame, text="Switch to Login", command=switch_to_login)
login_button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
