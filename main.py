from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import pyperclip
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
    if len(site) == 0 or len(the_password) == 0:
        messagebox.showwarning(title="Warning", message="Do not leave any fields empty.")
    else:
        question = f"Are these correct? \nEmail/Username: {email_username_input} \nPassword: {the_password}"
        if messagebox.askyesno(title=site, message=question):
            with open("password_manager_data.txt", "a") as file:
                file.write(f"{site} | Email/Username = {email_username_input} | Password = {the_password}\n")
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

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
website.focus()

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
