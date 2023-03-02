import tkinter as tk
import smtplib
import math
import random
from tkinter import messagebox

def login_screen():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('750x400')
    window.maxsize(950,600)
    window.minsize(950,600)

    global lbl_passcorr,entered_password,entered_username

    #First Frame
    frm_form = tk.Frame(window, background="#1d8cb9")
    frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)

    frm_form.rowconfigure([1],weight=1)
    frm_form.columnconfigure([1])

    #Second Frame
    frm_form_two = tk.Frame(frm_form,background="white",width=400,height=20)
    frm_form_two.grid(row=1,column=2,padx=300,pady=(200,250),sticky='nsew')

    #Username label_entry
    entered_username = tk.StringVar()
    lbl_first_name = tk.Label(frm_form_two, text="Username:",font=("Helvitca",12),background="white",width=10,foreground="grey")
    ent_first_name = tk.Entry(frm_form_two,textvariable=entered_username,width=25,relief=tk.SOLID,borderwidth=0)

    lbl_first_name.grid(row=0, column=0, sticky="e",pady=(10,0),padx=(10,0))
    ent_first_name.grid(row=0, column=1,pady=(10,0),padx=10)

    #Password label_entry
    entered_password = tk.StringVar()
    lbl_first_name = tk.Label(frm_form_two, text="Password:",font=("Helvitca",12),background="white",width=10,foreground="grey")
    ent_first_name = tk.Entry(frm_form_two,textvariable=entered_password,width=25,borderwidth=0)

    lbl_first_name.grid(row=1, column=0, sticky="e",pady=(10,0),padx=(10,0))
    ent_first_name.grid(row=1, column=1,pady=(10,0),padx=10)

    #error success msg label_entry
    lbl_passcorr = tk.Label(frm_form_two,font=("Helvitca",12),background="white")
    lbl_passcorr.grid(row=3, column=0,pady=(10,0),columnspan=2)

    #Buttons
    btn_register = tk.Button(frm_form_two,text="Register",borderwidth=0,command=registration_screen)
    btn_login = tk.Button(frm_form_two,text="Login",borderwidth=0,command=OTP_verification)
    
    btn_register.grid(row=2,column=0,sticky="e",pady=10)
    btn_login.grid(row=2,column=1,sticky="w",padx=(10,0),pady=10)

    window.mainloop()

    

def users():
    
    if password.get() == password_2.get():
        user_list = [first_name.get(),last_name.get(),email.get(),id.get(),username.get(),password.get(),password_2.get(),address.get(),city.get(),province.get()]

        with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','w') as filename:
            filename.write(' '.join(user_list))
        #delete entries
        ent_first_name.delete(0,tk.END),ent_last_name.delete(0,tk.END),ent_email.delete(0,tk.END),ent_id.delete(0,tk.END),
        ent_password.delete(0,tk.END),ent_password_2.delete(0,tk.END),ent_address1.delete(0,tk.END),ent_city.delete(0,tk.END),ent_province.delete(0,tk.END),ent_username.delete(0,tk.END)

        lbl_errsucc.config(text="Registration successful!",foreground="#5bf558")
    else:
        lbl_errsucc.config(text="Password must be the the same!",foreground="#f77c7c")
    

def registration_screen():

    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('750x400')
    window.maxsize(950,600)
    window.minsize(950,600)

    global first_name,last_name,email,id,password,password_2,address,city,province,username
    global ent_first_name,ent_last_name,ent_email,ent_id,ent_password,ent_password_2,ent_address1,ent_city,ent_province,ent_username
    global lbl_errsucc

    frm_form = tk.Frame(window, background="#1d8cb9")
    frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)

    frm_form_two = tk.Frame(frm_form,background="white",width=400,height=500)
    frm_form_two.grid(padx=290,pady=(50,0))
    
    #Registration
    lbl_first_name = tk.Label(frm_form_two, text="Register Here:",font=("Helvitca",16),background="white",foreground="grey")
    lbl_first_name.grid(row=0, column=0,columnspan=2,pady=10)

    #First_name label_entry
    first_name = tk.StringVar()
    lbl_first_name = tk.Label(frm_form_two, text="First Name:",font=("Helvitca",12),background="white",foreground="grey")
    ent_first_name = tk.Entry(frm_form_two,textvariable=first_name,width=25,borderwidth=0)

    lbl_first_name.grid(row=1, column=0, sticky="e",pady=(10,0))
    ent_first_name.grid(row=1, column=1,pady=(10,0),padx=10)

    #Last_name label_entry
    last_name = tk.StringVar()
    lbl_last_name = tk.Label(frm_form_two, text="Last Name:",font=("Helvitca",12),background="white",foreground="grey")
    ent_last_name = tk.Entry(frm_form_two,textvariable=last_name,width=25,borderwidth=0)

    lbl_last_name.grid(row=2, column=0, sticky="e",pady=(10,0))
    ent_last_name.grid(row=2, column=1,pady=(10,0),padx=10)
    
    #Email label_entry
    email = tk.StringVar()
    lbl_email = tk.Label(frm_form_two, text="Email:",font=("Helvitca",12),background="white",foreground="grey")
    ent_email = tk.Entry(frm_form_two,textvariable=email,width=25,borderwidth=0)

    lbl_email.grid(row=3, column=0, sticky="e",pady=(10,0))
    ent_email.grid(row=3, column=1,pady=(10,0),padx=10)

    #ID(Number) label_entry
    id = tk.StringVar()
    lbl_id = tk.Label(frm_form_two, text="ID(Number):",font=("Helvitca",12),background="white",foreground="grey")
    ent_id = tk.Entry(frm_form_two,textvariable=id,width=25,borderwidth=0)

    lbl_id.grid(row=4, column=0, sticky="e",pady=(10,0))
    ent_id.grid(row=4, column=1,pady=(10,0),padx=10)

    #Usename label_entry
    username = tk.StringVar()
    lbl_username = tk.Label(frm_form_two, text="Username:",font=("Helvitca",12),background="white",foreground="grey")
    ent_username = tk.Entry(frm_form_two,textvariable=username,width=25,borderwidth=0)

    lbl_username.grid(row=5, column=0, sticky="e",pady=(10,0))
    ent_username.grid(row=5, column=1,pady=(10,0),padx=10)
    
    #Password label_entry
    password = tk.StringVar()
    lbl_password = tk.Label(frm_form_two, text="Password:",font=("Helvitca",12),background="white",foreground="grey")
    ent_password = tk.Entry(frm_form_two,textvariable=password,width=25,borderwidth=0)

    lbl_password.grid(row=6, column=0, sticky="e",pady=(10,0))
    ent_password.grid(row=6, column=1,pady=(10,0),padx=10)

    password_2 = tk.StringVar()
    lbl_password_2 = tk.Label(frm_form_two, text="Password(Conf.):",font=("Helvitca",12),background="white",foreground="grey")
    ent_password_2 = tk.Entry(frm_form_two,textvariable=password_2,width=25,borderwidth=0)

    lbl_password_2.grid(row=7, column=0, sticky="e",pady=(10,0))
    ent_password_2.grid(row=7, column=1,pady=(10,0),padx=10)

    #Address label_entry
    address = tk.StringVar()
    lbl_address1 = tk.Label(frm_form_two, text="Address:",font=("Helvitca",12),background="white",foreground="grey")
    ent_address1 = tk.Entry(frm_form_two,textvariable=address,width=25,borderwidth=0)

    lbl_address1.grid(row=8, column=0, sticky="e",pady=(10,0))
    ent_address1.grid(row=8, column=1,pady=(10,0),padx=10)

    #City label_entry
    city = tk.StringVar()
    lbl_city = tk.Label(frm_form_two, text="City:",font=("Helvitca",12),background="white",foreground="grey")
    ent_city = tk.Entry(frm_form_two,textvariable=city,width=25,borderwidth=0)

    lbl_city.grid(row=9, column=0, sticky=tk.E,pady=(10,0))
    ent_city.grid(row=9, column=1,pady=(10,0),padx=10)

    #Country label_entry
    province = tk.StringVar()
    lbl_province = tk.Label(frm_form_two, text="Province:",font=("Helvitca",12),background="white",foreground="grey")
    ent_province = tk.Entry(frm_form_two,textvariable=province,width=25,borderwidth=0)

    lbl_province.grid(row=10, column=0, sticky=tk.E,pady=(10,0))
    ent_province.grid(row=10, column=1,pady=(10,0),padx=10)

    #Buttons
    btn_register = tk.Button(frm_form_two,text="Register",borderwidth=0,command=users)
    btn_login = tk.Button(frm_form_two,text="Login",borderwidth=0,command=login_screen)
    
    btn_register.grid(row=11,column=0,sticky="e",pady=10)
    btn_login.grid(row=11,column=1,sticky="w",padx=(10,0),pady=10)

    #error success msg label_entry
    lbl_errsucc = tk.Label(frm_form_two,font=("Helvitca",12),background="white")
    lbl_errsucc.grid(row=12, column=0,pady=(10,0),columnspan=2)
    
    
    window.mainloop()

def send_email():

    global OTP

    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]

    otp = OTP + " is your OTP"
    msg= otp

    with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
                user = filename.read().split(" ")

    emailid = user[2]

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("phefadutshepo8@gmail.com","kdlryqeebihngbuk")
    s.sendmail('&&&&&&&&&&',emailid,msg)
    s.quit()

def otp_confirm():
    otp_input = otp.get()

    if otp_input == OTP:
        voting_poles()
    else:
        lbl_wrnotp.config(text="Wrong OTP!",foreground="#f77c7c")



def OTP_verification():
    with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
                user = filename.read().split(" ")

    if entered_password.get() == user[5] and entered_username.get() == user[4]:
        for widget in window.winfo_children():
            widget.destroy()

        window.geometry('750x400')
        window.maxsize(950,600)
        window.minsize(950,600)

        global otp,lbl_wrnotp

        # with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
        #         user = filename.read()
    
        frm_form = tk.Frame(window, background="#1d8cb9")
        frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)

        frm_form_two = tk.Frame(frm_form,background="white",width=400,height=20)
        frm_form_two.grid(padx=320,pady=(200,0))

        #OTP label_entry
        otp = tk.StringVar()
        lbl_first_topmsg = tk.Label(frm_form_two,text='OTP sent your email:',foreground='grey',background='white',font=("Helvitca",12))
        lbl_otp = tk.Label(frm_form_two,text="Enter OTP",font=("Helvitca",12),foreground="grey",background="white")
        ent_otp = tk.Entry(frm_form_two,textvariable= otp,width=15,borderwidth=0)

        lbl_first_topmsg.grid(row=0, column=0,columnspan=2,padx=(10,0),sticky='w')
        lbl_otp.grid(row=1, column=0, sticky="e",pady=(10,0),padx=(10,0))
        ent_otp.grid(row=1, column=1,pady=(10,0),padx=10,sticky='w')

        #error success msg label_entry
        lbl_wrnotp = tk.Label(frm_form_two,font=("Helvitca",12),background="white")
        lbl_wrnotp.grid(row=3, column=0,pady=(0,10),columnspan=2)

        #Buttons
        btn_login = tk.Button(frm_form_two,text="Confirm",borderwidth=0,command=otp_confirm)
        btn_login.grid(row=2,column=1,sticky="w",padx=(10,0),pady=10)
        
        send_email()

        window.mainloop()
    else:
        lbl_passcorr.config(text="Wrong password!",foreground="#f77c7c")
        window.mainloop()

# def voting_poles():
#     for widget in window.winfo_children():
#         widget.destroy()

#     window.geometry('750x400')
#     window.maxsize(950,600)
#     window.minsize(950,600)

#     global btn_term,varv

#     frm_form = tk.Frame(window, background="#1d8cb9")
#     frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
#     #header
#     lbl_pole_name = tk.Label(frm_form, text="Select a pole to vote:",font=("Helvitca",30))
#     lbl_pole_name.grid(row=0,column=0,sticky="nsew",pady=(10,0),padx=(20,50),ipady=10)
    
#     #Poles label_entry
#     btn_term = tk.Button(frm_form, text="Second Term Elections",font=("Helvitca",20),width=50,height=3,borderwidth=0,command=vote_screen)
#     btn_term.grid(row=1, column=0, sticky="nsew",padx=(50,60),pady=(20,0))

#     window.mainloop()

def voting_poles():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('750x400')
    window.maxsize(950,600)
    window.minsize(950,600)

    global btn_term,varv

    frm_form = tk.Frame(window, background="#1d8cb9")
    frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
    #header
    lbl_pole_name = tk.Label(frm_form, text="Select a pole to vote:",font=("Helvitca",30))
    lbl_pole_name.grid(row=0,column=0,sticky="nsew",pady=(10,0),padx=(20,50),ipady=10)
    
    #Poles label_entry
    btn_term = tk.Button(frm_form, text="Second Term Elections",font=("Helvitca",20),width=50,height=3,borderwidth=0,command=vote_screen)
    btn_term.grid(row=1, column=0, sticky="nsew",padx=(50,60),pady=(20,0))

    with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
                user = filename.read().split(" ")
 
    if user[2] in list_voted:
        btn_term["state"] = tk.DISABLED
    # if varv.get() != "":
    #     btn_term["state"] = tk.DISABLED

    window.mainloop()

def users_voted(): 
    global list_voted
    list_voted = []


def vote_screen():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('750x400')
    window.maxsize(950,600)
    window.minsize(950,600)

    global varv,lbl_errvote

    frm_form = tk.Frame(window, background="#1d8cb9")
    frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)

    frm_form_two = tk.Frame(frm_form,background="white",width=400,height=20)
    frm_form_two.grid(padx=300,pady=(200,0))

    varv = tk.StringVar()
    #Voting options
    lbl_one = tk.Label(frm_form_two,text="EFF",font=("Helvitca",12),width=18,background="#34aeeb")
    rdb_one = tk.Radiobutton(frm_form_two,variable=varv,value='EFF',width=2,background="#34aeeb",activebackground="#34aeeb",borderwidth=0)

    lbl_one.grid(row=0,column=0,ipady=5,pady=10,padx=(10,0))
    rdb_one.grid(row=0,column=1,ipady=7,pady=10,padx=10)

    lbl_two = tk.Label(frm_form_two,text="ANC",font=("Helvitca",12),width=18,background="#34aeeb")
    rdb_two = tk.Radiobutton(frm_form_two,variable=varv,value='ANC',width=2,background="#34aeeb",activebackground="#34aeeb",borderwidth=0)

    lbl_two.grid(row=1,column=0,ipady=5,pady=(0,10),padx=(10,0))
    rdb_two.grid(row=1,column=1,ipady=7,pady=(0,10),padx=10)

    lbl_three = tk.Label(frm_form_two,text="COSATU",font=("Helvitca",12),width=18,background="#34aeeb")
    rdb_three = tk.Radiobutton(frm_form_two,variable=varv,value='COSATU',width=2,background="#34aeeb",activebackground="#34aeeb",borderwidth=0)

    lbl_three.grid(row=2,column=0,ipady=5,pady=(0,10),padx=(10,0))
    rdb_three.grid(row=2,column=1,ipady=7,pady=(0,10),padx=10)

    lbl_four = tk.Label(frm_form_two,text="DA",font=("Helvitca",12),width=18,background="#34aeeb")
    rdb_four = tk.Radiobutton(frm_form_two,variable=varv,value='DA',width=2,background="#34aeeb",activebackground="#34aeeb",borderwidth=0)

    lbl_four.grid(row=3,column=0,ipady=5,pady=(0,10),padx=(10,0))
    rdb_four.grid(row=3,column=1,ipady=7,pady=(0,10),padx=10)

    #error success msg label_entry
    lbl_errvote = tk.Label(frm_form_two,font=("Helvitca",12),background="white")
    lbl_errvote.grid(row=5, column=0,pady=(10,0),columnspan=2)

    #Buttons
    btn_vote = tk.Button(frm_form_two,text="Vote",width=10,borderwidth=0,command=confirmation_screen)  
    btn_vote.grid(row=4,column=0,pady=(0,10),columnspan=2)

    window.mainloop()

# def change_state():
#     global btn_term
#     btn_term["state"] = tk.DISABLED

def messages_screen():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('750x400')
    window.maxsize(950,600)
    window.minsize(950,600)

    frm_form = tk.Frame(window, background="#1d8cb9")
    frm_form.pack(fill=tk.BOTH, side=tk.TOP,expand=True)

    frm_form_two = tk.Frame(frm_form,background="white",width=400,height=60)
    frm_form_two.grid(padx=300,pady=(200,0))

    #Widget
    # if id_number in id_numbers:
    #    first_message
    # else:
    #    secon_message

    lbl_message = tk.Label(frm_form_two,text="You have registered!")
    lbl_message.grid(row=0,column=0,columnspan=2,ipadx=70,ipady=50)

    #Buttons
    btn_resend = tk.Button(frm_form_two,text="Resend",borderwidth=0,command=send_voteemail)
    btn_quit = tk.Button(frm_form_two,text="Quit",borderwidth=0,command=login_screen)
    
    btn_resend.grid(row=1,column=0,sticky="e",pady=10)
    btn_quit.grid(row=1,column=1,sticky="w",padx=(10,0),pady=10)

    window.mainloop()

def send_voteemail():
    with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
                user = filename.read().split(" ")  

    emailid = user[2]
    msgvote = f'The party you voted for is {varv.get()}'

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("mmaka5997@gmail.com","zqeoppfzejrxodbg")
    s.sendmail('&&&&&&&&&&',emailid,msgvote)
    s.quit()
    


def confirmation_screen():
    global list_voted
    
    if varv.get() != "":
        choice = tk.messagebox.askokcancel("Confirmation","Confirm your vote!")
        if choice == True:
            with open('/home/wethinkcode/Desktop/Pracs/MyPP/VotingSystem/users.txt','r') as filename:
                user = filename.read().split(" ")  
            list_voted.append(user[2])
            send_voteemail()
            messages_screen()
    else:
        lbl_errvote.config(text="Please choose an option!",foreground="#f77c7c")
        

#Start of the main window
window = tk.Tk()
window.title("Voting System")
window.minsize(950,600)
window.maxsize(950,600)
window.geometry("1500x800")



if __name__ == '__main__':
    users_voted()
    login_screen()