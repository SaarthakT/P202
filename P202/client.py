import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        Window = Tk()
        Window.withdraw()

        login = Toplevel()
        login.title("Login")

        login.resizable(width=False, height=False)
        login.configure(width=400, height=300)
        
        pls = Label(login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
        pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        labelName = Label(login,
							text = "Name: ",
							font = "Helvetica 12")
        labelName.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)

        entryName = Entry(login,
							font = "Helvetica 14")
        entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
        entryName.focus()
    def goAhead (self,name):
        self.login.destroy()
        self.name=name
        rcv = Thread(target=self.revieve)
        self.rcv.start()

    def receive():
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass()
            except:
                print("An error occured!")
                client.close()
                break

g = GUI()

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()
