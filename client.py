#Chatter v2 | Client
#|||||||||||||||||||||||||||||||||||||||||||||||
from ctypes import pointer
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import BOTTOM, DOTBOX, PhotoImage, messagebox as mgs, Canvas
from tkinter.ttk import *
import progressbar #pip install progressbar
import time
import sys

version = b"2.0"
version_without_byte = "2.0"

bar = progressbar.ProgressBar(maxval=10, widgets=[
    'Загрузка...| ',
    progressbar.Bar(left='[', marker='|', right=']'),
    progressbar.SimpleProgress(),
]).start()
t = 0.0
while t <= 10.0:
    bar.update(t)
    time.sleep(0.01)
    t += 0.1
bar.finish()


def connection():
    connect = input('Напишите номер комнаты (через #) : ')

    if connect != "#1":
        while 1:
            print('Неверный код комнаты!, повторите попытку')
            connection()
    else:
        ADDR = ('localhost', 7777)
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(ADDR)
        BUFSIZ = 1024

        client_socket.send(version)

        time.sleep(0)

        def receive():
            while True:
                try:
                    msg = client_socket.recv(BUFSIZ).decode("utf8")
                    if msg == 'Client version -> 1.0':
                        version_crash_by_server()
                    else:
                        msg_list.insert(tkinter.END, msg)
                except OSError:
                    break


        def send(event=None):
            msg = my_msg.get()
            my_msg.set("")
            client_socket.send(bytes(msg, "utf8"))
            if msg == "{quit}":
                mgs.showinfo('Чаттер', 'Вы вышли из чата!')
                client_socket.send(bytes('', "utf8"))
                client_socket.close()
                top.quit()
                top.destroy()
                exit()

        def version_crash_by_server():
            mgs.showerror('Error 10x09','Обновите приложение, у вас старая версия =(\nВы отсоеденены от сервера.')



        def on_closing(event=None):
            my_msg.set("{quit}")
            send()
            top.quit()
            top.destroy()
            exit()


        top = tkinter.Tk()
        top.title("Чаттер")
        top.wm_attributes('-alpha',0.9)
        top.iconbitmap('images/chat.ico')
        top['bg'] = '#17202A' #ccc
        top.resizable(width = False, height = False)
        top.geometry('500x390+400+170')

        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar() 
        my_msg.set("")
        scrollbar = tkinter.Scrollbar(messages_frame)  
        msg_list = tkinter.Listbox(messages_frame, height=15, width=54,bg='#2C3E50',fg='#EAECEE', font="Helvetica 13 bold", yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(top, font="Helvetica 13 bold",bg='#2C3E50',fg='#EAECEE',width=20,justify='center',textvariable=my_msg)
        entry_field.bind("<Return>", send)
        entry_field.pack(pady=22)

        #canvas = Canvas(top, width=600, height=600,bg="#17202A", highlightthickness=0)
        #canvas.pack()

        send_button = PhotoImage(file="images/send_button.png")
        send_button = send_button.subsample(7,7)
        #id_img1 = canvas.create_image(100,100, anchor="nw", image=send_button)
        #send_button_image = Button(top, image=send_button, width=10).pack(side=BOTTOM)

        send_button2 = tkinter.Button(top, image=send_button,height=35,width=46,bg="#17202A",command=send)
        send_button2.place(x=357, y=320)

        top.protocol("WM_DELETE_WINDOW", on_closing)

        receive_thread = Thread(target=receive)
        receive_thread.start()
        tkinter.mainloop()

connection()