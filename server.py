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

min_client_version = "2.0"
banned_versions = "1.0"
 
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

global clients
global addresses

clients = {}
addresses = {}
    

def accept_incoming_connections():
    while True:
        global client
        client, client_address = SERVER.accept()
        client_version_check()
        print(Fore.YELLOW+"%s:%s Присоединился(-ась) в чат." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def client_version_check():
    accepted_version_info = client.recv(BUFSIZ).decode("utf8")
    print("__________VERSION INFO____________\n"+accepted_version_info)
    while 1:
        if accepted_version_info == min_client_version:
            client.send(bytes("Вы зашли в чат! Напишите ваш никнейм!", "utf8"))
            break
        else:
            client.send(bytes("Client version -> "+banned_versions,"utf-8"))
            del clients[client]
            break
    

def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = '\n[SERVER] Привет %s,чтобы выйти напишите {quit}' % name
    client.send(bytes(welcome, "utf8"))
    msg = "[SERVER] %s Присоединился(-ась) в чат!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg,name+": ")
        elif msg == bytes("{quit}", "utf8"):
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes(f"[SERVER] {name} вышел(-а) из чата.", "utf8"))
        else:
            broadcast(msg,name+": ")


def broadcast(msg, prefix=""):

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

room = '#1'
HOST = 'localhost'
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