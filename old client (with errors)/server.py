#Chatter v2 | Server
#|||||||||||||||||||||||||||||||||||||||||||||||
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
import progressbar
import time
from colorama import init
from colorama import Back,Fore,Style
init()
 
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
time.sleep(2)

clients = {}
addresses = {}

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print(Fore.YELLOW+"%s:%s Присоединился(-ась) в чат." % client_address)
        client.send(bytes("Вы зашли в чат! Напишите ваш никнейм!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()



def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = '[SERVER] Привет %s,чтобы выйти напишите {quit}' % name
    client.send(bytes(welcome, "utf8"))
    msg = "[SERVER] %s Присоединился(-ась) в чат!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg,name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("[SERVER] %s вышел(-а) из чата." % name, "utf8"))
            break


def broadcast(msg, prefix=""):

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

room = '#1'
HOST = '192.168.0.102' #10.110.159.209
PORT = 7777
BUFSIZ = 1024
ADDR = (HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print(Fore.GREEN +"|------------Сервер Запущен----------------|")
    print(Fore.RED +'Ваш код комнаты '+Fore.YELLOW+'=> ' +Fore.CYAN+room)
    time.sleep(1)
    print(Fore.BLUE+'|------------Соединения----------------|')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
