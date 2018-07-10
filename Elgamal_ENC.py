import tkFileDialog as filedialog
from  Tkinter import *
import random
from Crypto.Util import number
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import codecs
import os
elg= 'elg.temp' 
global tt


def modexp( base, exp, modulus ):
		return pow(base, exp, modulus)

def find_primitive_root( p ):
		if p == 2:
				return 1
		p1 = 2
		p2 = (p-1) // p1
		while( 1 ):
				g = random.randint( 2, p-1 )

				if not (modexp( g, (p-1)//p1, p ) == 1):
						if not modexp( g, (p-1)//p2, p ) == 1:
								return g


def encrypt(alpha,beta,message,p):
    k=random.randint(1,p-2)   
    encoded_msg = bytearray(message, 'utf-8') 
    
    #encoded_msg=message
    
   # for w in message:
       # encoded_msg.append(ord(w))
    
    #encoded_msg.decode('utf-8')    
    y1=[]
    y2=[]
    #print encoded_msg
    
    for x in encoded_msg:
        y1.append(modexp(alpha,k,p))
       # print y1
        y2.append(((x%p)*modexp(beta,k,p))%p)
        #print y2
    
    print "encrypted message"
    print 'y1...'
    print y1
    print 'y2...'
    print y2
    
    return y1,y2

def elgamal_decrypt():
    win.destroy()
    root=Tk()
    root.fileName = filedialog.askopenfilename( filetypes= ( ("All files","*.*"),("text files","*.txt" ) ) )
    with open(root.fileName,"r+") as myfile:
        message = myfile.read()
    root.destroy()
    
    print message
    
    y1=[]
    ln=len(message)
    flag=False
    strng=""
    for i in range(0,ln):
        if message[i]=='x':
            flag=True
            
        elif flag==True:
            strng+=message[i]
        
        elif message[i]=='p' and flag==False:
            print(strng)
            y1.append(int(strng))
            strng=""
        else:
            strng+=message[i]
            
    print y1 
    ciphertext=strng
    ln=len(ciphertext)
    strng=""
    y2=[]
    for i in range(0,ln):
        if ciphertext[i]=='p':
            print(strng)
            y2.append(int(strng))
            strng=""
        else:
            strng+=ciphertext[i]
    
    print y2
    with open(elg,'r+') as f:
        
        num_lines = sum(1 for line in open(elg))
        data = f.readlines()
    
    
    for i in range(0,num_lines):
        if tt==i:
            k=data[i+2].rstrip()
            kk=data[i+3].rstrip()
   
        
    
    p=int(kk)
    prvt_key=int(k)
    print p
    print prvt_key
    
    d=[]
    
    for i,j in zip(y1,y2):
        d.append((((j%p)*modexp(i,p-1-prvt_key,p))%p))
    
    print 'decrypt...'
    rslt=""
    print d
    for i in d:
        rslt+=chr(i)
    print "Decrypted message:"
    print rslt
    with open(root.fileName,"r+") as myfile:
        myfile.truncate()
        myfile.write(rslt)
        #message = myfile.read()

def elgamal_encrypt():
    print tt
    win.destroy()
    val =300
    i=0
    with open(elg) as f:
        num_lines = sum(1 for line in open(elg))
    print num_lines
    if num_lines==0:
         while True:
             with open(elg,'a') as f: 
                 f.write('XYZ') 
                 f.write('\n')
                 f.write('XYZ')
                 f.write('\n')
                 i=i+2
                 if i==val:
                     break
    
    
    
    
    
    
    
    print "EL GAMAL Encrypter/ Decrypter"
    
    n_length = 32

    p = number.getPrime(n_length)
    
    print 'prime p....'
    print p
    
    
    print "primitive root of prime p........"
    alpha = find_primitive_root( p )
    print alpha
    
    prvt_key = random.randint( 1, p-2 )
    
    print 'private key.....'
    print prvt_key
    
    print "beta:...."
    beta = modexp(alpha,prvt_key,p)
    print beta
    
    one=str(alpha)
    two=str(beta)
    prv=str(prvt_key)
    pub=str(p)
    
    i = 0
    with open(elg,'r+') as f:
        num_lines = sum(1 for line in open(elg))
        data = f.readlines()
        
    print num_lines 
    
    while True: 
        if tt==i:
            data[i]=one+'\n'
            data[i+1]=two+'\n'
            data[i+2]=prv+'\n'
            data[i+3]=pub+'\n'
        i=i+4
        if i>num_lines:
            break
        
    with open(elg,'r+') as f:
        f.writelines(data)
    
    
    
    
    
    root = Tk()
    #root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))
    root.fileName = filedialog.askopenfilename( filetypes= ( ("All files","*.*"),("text files","*.txt" ) ) )
    with open(root.fileName,"r+") as myfile:
        message = myfile.read()
    
    root.destroy()
    print "message is...."
    #message=b
    print message

    print "msg printed"
    y1,y2=encrypt(alpha,beta,message,p)
    #print(y1)
   # strng1=str(y1)
    #strng2=str(y2)
    #print(strng1)
    #print(strng1)
    
    b=list(y1)
    print "List printed"
    print(b)
    ln=len(b)
    
    print(ln)
    
    string=""
   # print("Here"+string)
    for i in range(0,ln):
        x1=str(b[i])
       # print(xx)
        x1=x1+'p'
        #print(xx)
        #print("previous"+string)
        string+=x1
    
    string+='x'
    #print string
    b= list (y2)
    ln=len(b)
   # print("Here"+string)
    for i in range(0,ln):
        x1=str(b[i])
       # print(xx)
        x1=x1+'p'
        #print(xx)
        #print("previous"+string)
        string+=x1
    
    with open(root.fileName,"r+") as myfile:
        myfile.write(string)
    
    
    print(string)
    
        
       

    
    #print decrypt(message,prvt_key,p)
    
def Call(yy):
    print "i am here"
    print yy
    global tt
    tt=yy
    global win 
    win=Tk()
    win.geometry('500x300')
    enc = Button(win, text="Encryption", command= elgamal_encrypt)
    enc.grid(columnspan=2, sticky=W)
    dec = Button(win, text="Decryption", command= elgamal_decrypt)
    dec.grid(columnspan=2, sticky=W)
    win.mainloop()
    