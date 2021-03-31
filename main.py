from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import pyperclip
import json


def find_password():
    website_name = website.get()
    try:
        with open("password_manager/password_manager_data.json", "r") as file:
            websites_dict = json.load(file)
            try:
                email_username_for_website = websites_dict[website_name]["email"]
                password_for_website = websites_dict[website_name]["password"]
                messagebox.showinfo(title=website_name, message=f"Email/Username: {email_username_for_website}\n"
                                                                f"Password: {password_for_website}")
            except KeyError:
                messagebox.showwarning(title="Error", message="No Details for the website exists.")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_numbers)] + \
                    [random.choice(numbers) for _ in range(nr_symbols)]
    random.shuffle(password_list)

    random_password = ""
    for char in password_list:
        random_password += char
    pyperclip.copy(random_password)
    password.insert(END, random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    site = website.get()
    email_username_input = email_username.get()
    the_password = password.get()
    new_data = {
        site: {
            "email": email_username_input,
            "password": the_password,
        }
    }
    if len(site) == 0 or len(the_password) == 0:
        messagebox.showwarning(title="Warning", message="Do not leave any fields empty.")
    else:
        try:
            with open("password_manager/password_manager_data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password_manager/password_manager_data.json", "w"):
                pass

            with open("password_manager/password_manager_data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)

            with open("password_manager/password_manager_data.json", "w") as file:
                file.write("{}")
        else:
            with open("password_manager/password_manager_data.json", "w") as file:
                json.dump(data, file, indent=4)
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white")
canvas.grid(row=0, column=1)
logo = ImageTk.PhotoImage(Image.open("password_manager/logo.jpg"))
canvas.create_image(100, 100, image=logo)

website_writing = Label(text="Website:")
website_writing.grid(row=1, column=0)

website = Entry(width=21)
website.grid(row=1, column=1)
website.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

email_username_writing = Label(text="Email/Username:")
email_username_writing.grid(row=2, column=0)

email_username = Entry(width=35)
email_username.grid(row=2, column=1, columnspan=2)

password_writing = Label(text="Password:")
password_writing.grid(row=3, column=0)

password = Entry(width=21)
password.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
