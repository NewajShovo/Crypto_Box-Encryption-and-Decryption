from Tkinter import *
import RSA_ENC
import os

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'
another= 'Public.temp'
elg= 'elg.temp' 
def Authenticate(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
    global secretkey
    global nameEL
    global pwordEL # More globals :D
    global rootA
    global pub
    global pubA
    val =100
    i=0
    with open(another) as f:
        num_lines = sum(1 for line in open(another))
    print num_lines
    if num_lines==0:
         while True:
             with open(another,'a') as f: 
                 f.write('XYZ')
                 f.write('\n')
                 f.write('XYZ')
                 f.write('\n')
                 i=i+2
                 if i==val:
                     break
            
        
 
    roots = Tk() # This creates the window, just a blank one.
    roots.geometry('500x200')
    roots.title('Password Has to Be a Prime Number in Order to Sign up\n') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='Welcome to The System') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=W) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W) # ^^
    #pub.grid(row=3, column=0, sticky=W)
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1) # ^^
    #pubA.grid(row=3,column=1)
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(row=3,columnspan=2, sticky=W)
    
    loginB = Button(roots, text=' Login ', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
        
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():

        
        
    with open(creds,'a') as f:
        num_lines = sum(1 for line in open(creds))
        if num_lines != 0:
            f.write('\n')
        
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        
    
        #data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        #num_lines = sum(1 for line in open(creds))
         
    f.close() # Closes the file
    roots.destroy() # This will destroy the signup window. :)
    #Authenticate() # This will move us onto the login definition :D
 
    

    
    
def CheckLogin():
    
    #print("hello")
    print(nameE.get())
    
    print(pwordE.get())
    with open(creds) as f:
        num_lines = sum(1 for line in open(creds))
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        #print(nameE)
        #print(pwordE)

        
        #roots.destroy()
        i=0;
        ans=0;
        flag=False
        while True:
            uname = data[i].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
            pword = data[i+1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
            if nameE.get() == uname and pwordE.get() == pword:
                ans=i
                flag=True
            i=i+2
            if i==num_lines:
                break;
        
        pword=pwordE.get()
    if flag:
        roots.destroy()
        RSA_ENC.go(pword,ans)# "logged in" label
        #rlbl.pack() 
        #r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 

 
if os.path.isfile(creds):
    Authenticate()
