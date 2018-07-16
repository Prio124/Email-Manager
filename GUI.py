from Tkinter import *
import smtplib

class MainApp:
    def __init__(self, root):
        #set root
        self.root = root
        #Top frame
        self.frame = Frame(root)
        self.frame.grid(column=0, row=0, columnspan=4, rowspan=4)
        #label 1 { Email : }
        self.lbl1 = Label(self.frame, text="Email :")
        self.lbl1.grid(column=0, row=0)
        #email
        self.email = StringVar()
        self.email.set("email...")
        self.ent1 = Entry(self.frame, textvariable=self.email)
        self.ent1.grid(column=1, row=0)
        #label 2 { Password : } 
        self.lbl2 = Label(self.frame, text="Password :")
        self.lbl2.grid(column=0, row=1)
        #password
        self.password = StringVar()
        self.ent2 = Entry(self.frame, show="*", textvariable=self.password)
        self.ent2.grid(column=1, row=1)
        #control label
        self.controlbl = Label(self.frame, text="")
        self.controlbl.grid(column=0, row=2)
        #button
        self.checkButton = Button(self.frame, text="LOGIN")
        self.checkButton.grid(column=1, row=2)
        self.checkButton.bind("<Button-1>", self.login)

    def login(self, event):
        try:
            server = smtplib.SMTP_SSL("smtp.libero.it", 465)
            server.login(self.email.get(), self.password.get())
            self.controlbl["text"] = "CORRECT DATA!"
            #destroying old frame
            self.frame.destroy()
            #creating a new frame
            SendEmail(self.root)
        except:
            self.controlbl["text"] = "WRONG DATA!"

class SendEmail:
    def __init__(self, root):
        self.top = Frame(root)
        self.top.grid()
        #label 1 { Email : }
        self.lbl1 = Label(self.top, text="Email :")
        self.lbl1.grid(column=0, row=0)
        
def main():
    root = Tk()
    root.title("Email Manager")
    mainApp = MainApp(root)
    root.mainloop()

main()
