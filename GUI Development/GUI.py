from tkinter import *
from mydb import Database

class NLPApp:

    def __init__(self):

        self.dbo = Database()

        # login ka gui load karna
        self.root = Tk()
        self.root.title('NLPApp')
        # self.root.iconbitmap('resource/github.png') generate favicon.ico image then it will add logo
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui() 

        self.root.mainloop()
    
    def login_gui(self):

        self.clear()

        heading = Label(self.root, text = 'NLPApp', bg = "#34495E")
        heading.pack(pady=(30,30))
        heading.configure(font= ('verdana', 24, 'bold'))

        label1 = Label(self.root, text = "Enter Email")
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root, width=25)
        self.email_input.pack(pady= (5,10), ipady = 4)
        
        label1 = Label(self.root, text = "Enter Password")
        label1.pack(pady = (10,10))

        self.password_input = Entry(self.root, width=25,show="*")
        self.password_input.pack(pady= (5,10), ipady = 4)

        login_btn = Button(self.root, text = 'Login', width=20)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text = "Not a member?")
        label3.pack(pady = (20,10))
        
        redirect_btn = Button(self.root, text = 'Register', width=20, command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text = 'NLPApp', bg = "#34495E")
        heading.pack(pady=(30,30))
        heading.configure(font= ('verdana', 24, 'bold'))

        label0 = Label(self.root, text = "Enter Name")
        label0.pack(pady = (10,10))

        self.name_input = Entry(self.root, width=25)
        self.name_input.pack(pady= (5,10), ipady = 4)

        label1 = Label(self.root, text = "Enter Email")
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root, width=25)
        self.email_input.pack(pady= (5,10), ipady = 4)
        
        label1 = Label(self.root, text = "Enter Password")
        label1.pack(pady = (10,10))

        self.password_input = Entry(self.root, width=25,show="*")
        self.password_input.pack(pady= (5,10), ipady = 4)

        login_btn = Button(self.root, text = 'Register', width=20, command=self.perform_registration)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text = "Already a member?")
        label3.pack(pady = (20,10))
        
        redirect_btn = Button(self.root, text = 'Login', width=20, command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
        # clear exsiting gui
        for i in self.root.pack_slaves(): # pack_slaves print all widgets(like lable1,2,3 and entry box etc)
            print(i.destroy())

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response == 1:
            print('Registration Successful')
        else:
            print('Email exists')

nlp = NLPApp()