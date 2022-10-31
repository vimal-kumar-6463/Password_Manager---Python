from tkinter import *
import random
font_ = ('imapct',10)


window = Tk()
def generate() :
    alph = "a b c d e f g h i j k l m n o p q r s t u v w z y x".split()
    nums = "1 2 3 4 5 6 7 8 9 0".split()
    spl_char = "! @ # $ % ^ & * ( ) _ + - = : ; , . < > ? / | [ ]".split()
    pass_alp = random.choices(alph , k = 4)
    pass_nums = random.choices(nums, k = 4)
    pass_spl_char = random.choices(spl_char,k = 2)
    cum_pass = pass_alp
    print(cum_pass)
    cum_pass.extend(pass_nums)
    print(cum_pass)
    cum_pass.extend(pass_spl_char)
    print(cum_pass)
    random.shuffle(cum_pass)
    print(cum_pass)
    ans = ""
    for i in cum_pass :
        ans += i
    generated_password.config(text = ans)
    print(cum_pass)
    
def add_to_file() :
    password_file = open("passwords.txt","a+")   
    password_file.write(f"\n{website_entry.get()}  ||  {email_entry.get()}  ||  {generated_password.cget('text')}") 
    password_file.close()
    status.config(text = "Added Successfully")
    with open("passwords.txt","r") as f :
        print(type(f.readlines()))
    

window.title("password_manager")
window.config(padx = 50 , pady = 50)

website_label = Label(window,text = "Website",font = font_)
website_label.grid(row = 0 , column = 0)
website_entry = Entry(window,font=font_)
website_entry.grid(row = 0 , column = 1)

email_label = Label(window,text = "Email",font = font_)
email_label.grid(row = 1 , column = 0)
email_entry = Entry(window,font=font_)
email_entry.grid(row = 1 , column = 1)

password_label = Label(window,text = "password",font = font_)
password_label.grid(row = 2 , column = 0)
generated_password = Label(window,font=font_,text="")
generated_password.grid(row = 2 , column = 1)
generate_btn = Button(window,font=font_,text="generate_password",command=generate)
generate_btn.grid(row = 2,column= 2)

add_btn = Button(window, font = font_, text = "add password to database",command= add_to_file)
add_btn.grid(row = 3 , column = 0)

status = Label(window,font = font_,text = "")
status.grid(row = 4 , column = 2)












window.mainloop()