from tkinter import *
from tkinter import messagebox
from pyperclip import copy, paste
import json
from password_generator import password_generator
import os
os.system('clear')


def read_passwords_file():
    with open(file='passwords.json', mode='r') as password_file:
        return json.load(fp=password_file)


def write_to_file(data_to_write):
    with open(file='passwords.json', mode='w') as file:
        json.dump(obj=data_to_write, fp=file, indent=4)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    copy(password)
    paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_password_to_save = {
        website: {
            'email': email_username,
            'password': password
        }
    }

    if website == '' or email_username == '' or password == '':
        messagebox.showerror(title='Error', message='Please do not leave any fields empty.')
    else:
        proceed = messagebox.askokcancel(title=website, message=f'Below are the credentials entered:\n\nWebsite: '
                                                                f'{website}\n\nEmail/Username: '
                                                                f'{email_username}\n\nPassword: {password}\n\nProceed?')

        if proceed:
            try:
                passwords = read_passwords_file()
            except FileNotFoundError:
                write_to_file(data_to_write=new_password_to_save)
            else:
                passwords.update(new_password_to_save)
                write_to_file(data_to_write=passwords)
            finally:
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                email_username_entry.insert(0, 'abhay.shrawankar@gmail.com')
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    try:
        passwords = read_passwords_file()
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No password file found.')
    else:
        website = website_entry.get()
        credentials = passwords.get(website)
        if credentials is not None:
            messagebox.showinfo(title=website, message=f'Below are the credentials:\n\nWebsite: {website}\nEmail: '
                                                       f'{credentials['email']}\nPassword: {credentials['password']}')
        else:
            messagebox.showinfo(title=website, message=f'{website} does not exist in the Password Manager.')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text='Search', width=13, command=search_password)
search_button.grid(column=2, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=38)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, 'abhay.shrawankar@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text='Generate Password', width=13, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
