__author__ = 'Cyber-01'
import socket
from PIL import Image
from PIL import ImageGrab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import webbrowser
import time
import cv2
import msvcrt
from  multiprocessing import Process
import pyHook
import pythoncom
import thread
import threading
from pynput.mouse import Button, Controller

my_socket_mouse = socket.socket()
ip = '192.168.30.34'

def main():
    my_socket = socket.socket()
    my_socket.connect((ip,1003))

    #thread.start_new_thread(mouse_reader, (my_socket_mouse, ))
    p = Process(target=mouse_reader)
    p.start()
    cv2.namedWindow("ImageWindow", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("ImageWindow", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        recv_photo = open(r"C:\Users\Public\Pictures\recv_photo.jpg",'wb')
        l = my_socket.recv(1024)
        while "finitosahartheking" not in l:
            recv_photo.write(l)
            l = my_socket.recv(1024)
        recv_photo.close()
        img = cv2.imread(r"C:\Users\Public\Pictures\recv_photo.jpg")
        cv2.imshow("ImageWindow", img)
        k = cv2.waitKey(1)
        if k == 27:
            break
        deleteconctent(r"C:\Users\Public\Pictures\recv_photo.jpg")

    my_socket.close()

def deleteconctent(fname):
    with open(fname, "w"):
        pass


def mouse_reader():
    hm = pyHook.HookManager()
    hm.MouseAll = OnMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()


def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'
    my_socket_mouse.connect((ip,1233))
    my_socket_mouse.send(event.Position)
    return True


if __name__=='__main__':
    main()