from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Авторизация')
window.geometry('400x600')
window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def clicked():
    username = username_entry.get()
    surname = surname_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    repassword = repassword_entry.get()
    messagebox.showinfo('Заголовок', '{username}, {password}, {surname}'.format(username=username, surname=surname, login=login, password=password, repassword=repassword))

main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

username_label = Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()

username_entry = Entry(window, bg='#fff', fg='#444',font=font_entry)
username_entry.pack()

surname_label = Label(window, text='Фамилия', font=label_font, **base_padding)
surname_label.pack()

surname_entry = Entry(window, bg='#fff', fg='#444',font=font_entry)
surname_entry.pack()

login_label = Label(window, text='Логин', font=label_font, **base_padding)
login_label.pack()

login_entry = Entry(window, bg='#fff', fg='#444',font=font_entry)
login_entry.pack()

password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

repassword_label = Label(window, text='Повтор пароля', font=label_font, **base_padding)
repassword_label.pack()

repassword_entry = Entry(window, bg='#fff', fg='#444',font=font_entry)
repassword_entry.pack()

send_btn = Button(window, text='Регистрация', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()
