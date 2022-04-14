#Chatter v2 | Client
#|||||||||||||||||||||||||||||||||||||||||||||||
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import *
import progressbar #pip install progressbar
import time

version = b'1.0'

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

connect = input('Напишите номер комнаты (через #) : ')

if connect == '#1':
	ADDR = ('192.168.0.102', 7777)
	client_socket = socket(AF_INET, SOCK_STREAM)
	client_socket.connect(ADDR)
	BUFSIZ = 1024

	time.sleep(0)

	def receive():
	    while True:
	        try:
	            msg = client_socket.recv(BUFSIZ).decode("utf8")
	            msg_list.insert(tkinter.END, msg)
				client_socket.send(version)
	        except OSError:
	            break


	def send(event=None):
	    msg = my_msg.get()
	    my_msg.set("")
	    client_socket.send(bytes(msg, "utf8"))
	    if msg == "{quit}":
	        client_socket.close()
	        top.quit()


	def on_closing(event=None):
	    my_msg.set("{quit}")
	    send()


	top = tkinter.Tk()
	top.title("Чаттер")
	top.wm_attributes('-alpha',0.9)
	top.iconbitmap('images/chat.ico')
	top['bg'] = '#ccc'
	top.resizable(width = False, height = False)
	top.geometry('370x300')

	messages_frame = tkinter.Frame(top)
	my_msg = tkinter.StringVar() 
	my_msg.set("")
	scrollbar = tkinter.Scrollbar(messages_frame)  
	msg_list = tkinter.Listbox(messages_frame, height=15, width=54, yscrollcommand=scrollbar.set)
	scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
	msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
	msg_list.pack()
	messages_frame.pack()

	entry_field = tkinter.Entry(top,font = '15', textvariable=my_msg)
	entry_field.bind("<Return>", send)
	entry_field.pack()
	send_button = tkinter.Button(top, text="Отправить", command=send)
	send_button.pack()

	#top.protocol("WM_DELETE_WINDOW", on_closing)

	receive_thread = Thread(target=receive)
	receive_thread.start()
	tkinter.mainloop()

else:
	print('Неверный код комнаты!')
	while True:
		connect = input('Напишите номер комнаты (через #) : ')
		if connect == '#1':
			ADDR = ('192.168.0.102', 7777)
			client_socket = socket(AF_INET, SOCK_STREAM)
			client_socket.connect(ADDR)
			BUFSIZ = 1024

			time.sleep(0)

			def receive():
			    while True:
			        try:
			            msg = client_socket.recv(BUFSIZ).decode("utf8")
			            msg_list.insert(tkinter.END, msg)
			        except OSError:
			            break


			def send(event=None):
			    msg = my_msg.get()
			    my_msg.set("")
			    client_socket.send(bytes(msg, "utf8"))
			    if msg == "{quit}":
			        client_socket.close()
			        top.quit()


			def on_closing(event=None):
			    my_msg.set("{quit}")
			    send()


			top = tkinter.Tk()
			top.title("Чаттер")
			top.wm_attributes('-alpha',0.9)
			top.iconbitmap('images/chat.ico')
			top['bg'] = '#ccc'
			top.resizable(width = False, height = False)
			top.geometry('370x300')

			messages_frame = tkinter.Frame(top)
			my_msg = tkinter.StringVar() 
			my_msg.set("")
			scrollbar = tkinter.Scrollbar(messages_frame)  
			msg_list = tkinter.Listbox(messages_frame, height=15, width=54, yscrollcommand=scrollbar.set)
			scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
			msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
			msg_list.pack()
			messages_frame.pack()

			entry_field = tkinter.Entry(top,font = '15', textvariable=my_msg)
			entry_field.bind("<Return>", send)
			entry_field.pack()
			send_button = tkinter.Button(top, text="Отправить", command=send)
			send_button.pack()

			#top.protocol("WM_DELETE_WINDOW", on_closing)

			receive_thread = Thread(target=receive)
			receive_thread.start()
			tkinter.mainloop()
		else:
			print('Неверный код комнаты!')
			while True:
				connect = input('Напишите номер комнаты (через #) : ')
				if connect == '#1':
					ADDR = ('85.113.39.69', 27015)
					client_socket = socket(AF_INET, SOCK_STREAM)
					client_socket.connect(ADDR)
					BUFSIZ = 1024

					time.sleep(0)

					def receive():
					    while True:
					        try:
					            msg = client_socket.recv(BUFSIZ).decode("utf8")
					            msg_list.insert(tkinter.END, msg)
					        except OSError:
					            break


					def send(event=None):
					    msg = my_msg.get()
					    my_msg.set("")
					    client_socket.send(bytes(msg, "utf8"))
					    if msg == "{quit}":
					        client_socket.close()
					        top.quit()


					def on_closing(event=None):
					    my_msg.set("{quit}")
					    send()


					top = tkinter.Tk()
					top.title("Чаттер")
					top.wm_attributes('-alpha',0.9)
					top.iconbitmap('images/chat.ico')
					top['bg'] = '#ccc'
					top.resizable(width = False, height = False)
					top.geometry('370x300')

					messages_frame = tkinter.Frame(top)
					my_msg = tkinter.StringVar() 
					my_msg.set("")
					scrollbar = tkinter.Scrollbar(messages_frame)  
					msg_list = tkinter.Listbox(messages_frame, height=15, width=54, yscrollcommand=scrollbar.set)
					scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
					msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
					msg_list.pack()
					messages_frame.pack()

					entry_field = tkinter.Entry(top,font = '15', textvariable=my_msg)
					entry_field.bind("<Return>", send)
					entry_field.pack()
					send_button = tkinter.Button(top, text="Отправить", command=send)
					send_button.pack()

					#top.protocol("WM_DELETE_WINDOW", on_closing)

					receive_thread = Thread(target=receive)
					receive_thread.start()
					tkinter.mainloop()
