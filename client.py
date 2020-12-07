# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:09:18 2020

@author: Nathan Russell
"""

import socket
import threading
import pyDH
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host,port))
                
                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.s.send(self.username.encode())
        
        message_handler = threading.Thread(target=self.handle_messages,args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()

    def handle_messages(self):
        while 1:
            
            cipher = AES.new(key, AES.MODE_CBC, IV) 
            decrypted = (cipher.decrypt(self.s.recv(1204).decode()), AES.block_size)
            print(decrypted)
            
    def input_handler(self):
        while 1:
            message = input()
            plaintext = AES.new(key, AES.MODE_CBC, IV)
            encrypted = (plaintext.encrypt(message, AES.block_size))
            self.s.send((self.username+' - '+encrypted.encode())

client = Client()