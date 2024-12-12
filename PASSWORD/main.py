from tkinter import messagebox
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

import random
def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters)]


        

        random.shuffle(password_list)

        password = "".join(password_list)

        password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   website = website_entry.get()
   email = email_entry.get()
   password = password_entry.get()

   if len(website) ==0 or len(password)==0:
     messagebox.showerror(title="Error", message="Please fill out all fields")
   else:
      is_ok=messagebox.askokcancel(title=website, message="You are going to add details. Is it Okay to sva?")
      if is_ok:
         with open('100Days-Python/PASSWORD/data.txt',"a") as data_file:
              data_file.write(f"{website} | {email} | {password} \n")
              website_entry.delete(0,END)
              password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PassWord manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="100Days-Python/PASSWORD/logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text = "Email:")
email_label.grid(row=2,column=0)

password_label = Label(text = "Password:")
password_label.grid(row=3, column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "abcd123@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


generate_password = Button(text="Generate Password")
generate_password.grid(row=3,column=2)

add_button = Button(text="Add",width=38, command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
