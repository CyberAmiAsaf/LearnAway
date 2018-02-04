__author__ = 'Cyber-01'
import socket
from PIL import ImageGrab
from PIL import Image
import mss
import webbrowser
import time
from multiprocessing import Process
import pyHook
import pythoncom
import pyscreeze
import pyautogui
from pathos.multiprocessing import ProcessingPool as Pool
import thread
import win32api, win32con

server_socket_mouse = socket.socket()
def main():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1003))
    server_socket.listen(1)
    client_socket,client_address = server_socket.accept()

    p = Process(target = mouse_control)
    p.start()

    #thread.start_new_thread( mouse_control, (server_socket_mouse , ) )
    while True:
        im = ImageGrab.grab()
        im.save(r"C:\Users\Public\Pictures\img.jpg")
        f = open(r"C:\Users\Pubonmlic\Pictures\img.jpg",'rb')
        print 'Sending...'
        l = f.read(1024)
        while (l):
            client_socket.send(l)
            l = f.read(1024)
        time.sleep(0.2)
        client_socket.send("finitosahartheking")


    client_socket.close()
    server_socket.close()


def mouse_control():
    server_socket_mouse.bind(('0.0.0.0', 1233))
    server_socket_mouse.listen(1)
    client_socket_mouse,client_address_mouse = server_socket_mouse.accept()
    while True:
        data = client_socket_mouse.recv(1024)
        print data
        print "king"

def OnMouseEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'
    return True



if __name__=='__main__':
    main()