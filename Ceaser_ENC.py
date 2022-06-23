from __future__ import with_statement
import os
another= 'Public.temp' 

import tkFileDialog as filedialog
from  Tkinter import *
import random
from Crypto.Util import number
from Crypto.PublicKey import RSA
global xx
global root

key = 'ABCDEFGHIJKLMNOPQERSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?#$`~><:";{}[]'
def caesar_encrypt():
    """Encrypt the string and return the ciphertext"""
    win.destroy()
    print len(key)
    n=3
    root=Tk()
    root.fileName = filedialog.askopenfilename( filetypes= ( ("All files","*.*"),("text files","*.txt" ) ) )
    root.destroy()
     #encrypted = caesar_encrypt(offset, root.fileName)
    
    with open(root.fileName,"r+") as myfile:
        message = myfile.read()
    
    result = ''
    for l in message:
        try:
            i = (key.index(l) + n) % 77
            result += key[i]
        except ValueError:
            result += l
            
    with open(root.fileName,"r+") as myfile:
        myfile.truncate()
        myfile.write(result)
    
    print result
    #return result

    


def caesar_decrypt():
    """Decrypt the string and return the plaintext"""
    win.destroy()
    n=3
    result = ''
    root=Tk()
    root.fileName = filedialog.askopenfilename( filetypes= ( ("All files","*.*"),("text files","*.txt" ) ) )
    root.destroy()
    with open(root.fileName,"r+") as myfile:
        message = myfile.read()

    for l in message:
        try:
            i = (key.index(l) - n) % 77
            result += key[i]
        except ValueError:
            result += l
            
    with open(root.fileName,"r+") as myfile:
        myfile.truncate()
        myfile.write(result)       
    print result



def Call():
    global win 
    win=Tk()
    win.geometry('500x300')
    enc = Button(win, text="Encryption", command= caesar_encrypt)
    enc.grid(columnspan=2, sticky=W)
    dec = Button(win, text="Decryption", command= caesar_decrypt)
    dec.grid(columnspan=2, sticky=W)
    win.mainloop()
