
from tkinter import *
from time import time, ctime
import json


GREEN = "#d1d4d4"
BLUE = "#4252d1"
GREY = "#2d2c2c"
WHITE = "#ffffff"
BLACK = "#252424"
RED = "#ce102a"
# global customer_name, address_entry, dropdown, dropdown2, dropdown3
# ticket_info: {
#     "customer": customer_name.get(),
#     "address": address_entry.get(),
#     "priority": dropdown.get(),
#     "category": dropdown2.get(),
#     "issue": dropdown3.get()
# }

# global customer_entry, address_entry, dropdown, dropdown2, dropdown3
# customer = customer_entry.get()
# address = address_entry.get()
# priority = dropdown.get()
# category = dropdown2.get()
# issue = dropdown3.get()


t = time()
login_success = False


with open("ticket_number.txt", "r") as ticket_number:
    tk_number = int(ticket_number.read())
    print(tk_number)

# with open("ticket_data.json", "w") as ticket_data:
#     json.dump(ticket_info, ticket_data)


def button_clicked():
    global tk_number
    tk_number += 1

def show_selected(selected_option):
    selection_label.config(text="Priority: ")

def type_selected(selected_option2):
    selection_label2.config(text="Category: ")
    update_third_dropdown(selected_option2)

def type_selected2(selected_option3):
    selection_label3.config(text="Issue: ")

def update_third_dropdown(selected_option2):
    if selected_option2 == "Email":
        var2.set(email_options[0])  # Set default option for Email
        dropdown3['menu'].delete(0, 'end')  # Clear existing options
        for option in email_options:
            dropdown3['menu'].add_command(label=option, command=lambda value=option: var2.set(value))
    elif selected_option2 == "Telephone":
        var2.set(tele_options[0])  # Set default option for Telephone
        dropdown3['menu'].delete(0, 'end')  # Clear existing options
        for option in tele_options:
            dropdown3['menu'].add_command(label=option, command=lambda value=option: var2.set(value))
    elif selected_option2 == "Internet":
        var2.set(internet_options[0])  # Set default option for Internet
        dropdown3['menu'].delete(0, 'end')  # Clear existing options
        for option in internet_options:
            dropdown3['menu'].add_command(label=option, command=lambda value=option: var2.set(value))






def login():
    # Replace these with your actual authentication logic
    valid_username = "admin"
    valid_password = "admin"

    entered_username = username_entry.get()
    entered_password = password_entry.get()


    if entered_username == valid_username and entered_password == valid_password:
        global login_success
        login_success = True
        login_window.destroy()
    else:
        error_label = Label(text="Incorrect Credentials", fg=RED, bg=GREEN, font=("arial", 9, 'normal'))
        error_label.grid(column=1, row=4)
login_window = Tk()
login_window.geometry("300x200")

username_label = Label(text="Username: ", fg=BLACK, bg=GREEN, font=("arial", 15, 'normal'))
username_label.grid(column=0, row=1)
username_entry = Entry()
username_entry.grid(column=1, row=1)
password_label = Label(text="Password: ", fg=BLACK, bg=GREEN, font=("arial", 15, 'normal'))
password_label.grid(column=0, row=2)
password_entry = Entry(show="*")
password_entry.grid(column=1, row=2)

login_submit_button = Button(text="Submit", command=login)
login_submit_button.grid(column=1, row=3)

login_window.mainloop()

if login_success:
    window = Tk()
    window.title("Tickets")
    window.configure(bg=GREEN)
    window.geometry("850x600")

    title = Label(text="Ticket Portal", fg=BLUE, bg=GREEN, font=("arial", 23, 'bold'))
    title.grid(column=1, row=0)
    tk_label = Label(text=f"Ticket #{tk_number}", fg=BLUE, bg=GREEN, font=("arial", 11, 'italic'))
    tk_label.grid(column=3, row=0)
    time_label = Label(text=ctime(t), fg=BLUE, bg=GREEN, font=("arial", 11, "normal"))
    time_label.grid(column=3, row=1)

    # Name
    customer_label = Label(text="Customer Name: ", fg=BLACK, bg=GREEN, font=("arial", 15, 'normal'))
    customer_label.grid(column=0, row=1, sticky=W)
    customer_name = Entry(width=40)
    customer_name.grid(column=1, row=1, sticky=W)
    # Address
    address_label = Label(text="Customer Address: ", fg=BLACK, bg=GREEN, font=("arial", 15, 'normal'))
    address_label.grid(column=0, row=2, sticky=W)
    address_entry = Entry(width=40)
    address_entry.grid(column=1, row=2, sticky=W)

    # Severity
    options = ["Low", "Medium", "High"]
    var = StringVar(window)
    var.set(options[0])  # default value

    dropdown = OptionMenu(window, var, *options, command=show_selected)
    dropdown.config(bg=WHITE, fg=BLACK, font=("Arial", 10))
    dropdown.grid(column=1, row=3, sticky=W)

    selection_label = Label(window, text="Priority: ", bg=GREEN, fg=BLACK, font=("Arial", 14))
    selection_label.grid(column=0, row=3, sticky=W)

    # Type of Trouble
    type_options = ["Email", "Telephone", "Internet"]
    var1 = StringVar(window)
    var1.set(type_options[0])  # default value

    dropdown2 = OptionMenu(window, var1, *type_options, command=type_selected)
    dropdown2.config(bg=WHITE, fg=BLACK, font=("Arial", 10))
    dropdown2.grid(column=1, row=4, sticky=W)

    selection_label2 = Label(window, text="Category: ", bg=GREEN, fg=BLACK, font=("Arial", 14))
    selection_label2.grid(column=0, row=4, sticky=W)

    # Type of Trouble Descriptive
    email_options = ["Incoming", "Outgoing", "Login", "Other"]
    tele_options = ["Incoming", "Outgoing", "No Dial Tone", "Endless Ring", "Static on Line", "Other"]
    internet_options = ["Slow Speeds", "Internet Down", "Other"]
    var2 = StringVar(window)
    var2.set("Select")  # default value
    dropdown3 = OptionMenu(window, var2, "", command=type_selected2)
    dropdown3.config(bg=WHITE, fg=BLACK, font=("Arial", 10))
    dropdown3.grid(column=1, row=5, sticky=W)

    selection_label3 = Label(window, text="Issue: ", bg=GREEN, fg=BLACK, font=("Arial", 14))
    selection_label3.grid(column=0, row=5, sticky=W)

    # Initialize options for the third dropdown based on the default value of the second dropdown
    update_third_dropdown(var1.get())

    # Notes
    notes_label = Label(text="Notes: ", fg=BLACK, bg=GREEN, font=("arial", 15, 'normal'))
    notes_label.grid(column=0, row=6, sticky=W)
    customer_note = Text(window, width=60, height=5)
    customer_note.grid(column=1, row=6, sticky=W)

    submit_button = Button(text="Submit", command=button_clicked)
    submit_button.grid(column=1, row=7)

  

    window.mainloop()


ticket_info: {
        "customer": customer_name.get(),
        "address": address_entry.get(),
        "priority": dropdown.get(),
        "category": dropdown2.get(),
        "issue": dropdown3.get()
    }

with open("ticket_data.json", "w") as ticket_data:
     json.dump(ticket_info, ticket_data)







