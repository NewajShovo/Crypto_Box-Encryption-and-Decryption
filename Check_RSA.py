# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:01:58 2018

@author: FM COMPUTER
"""



#from Crypto.Util import number

#n_length = 2048

#primeNum =RSA.generate(1024)


'''
620031587
Net-Centric Computing Assignment
Part A - RSA Encryption
'''

import random
from Crypto.Util import number
from Crypto.PublicKey import RSA

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''
def miller_rabin(n, k=10):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in xrange(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True




def generate_keypair(p, q):
    if not (miller_rabin(p) and  miller_rabin(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def encrypt(val,pk, plaintext):
   # print(val)
    #Unpack the key into it's components
    #print(pk)
    n=val
    #print("PPPPPPPPPPPPPPPP")
    #print(plaintext)
   # for char in plaintext:
        #pow(ord(char),pk,val)
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow_mod(ord(char),pk,n) for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(val,pk, ciphertext):
    #Unpack the key into its components
    #print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    n = val
        
        
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow_mod(char,pk,n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    return plain

def decrypt1(pk, ciphertext):
    #print(ciphertext)
    print("I am here")
    key, n = pk
    print(ciphertext)
    
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    ln=len(ciphertext)
    print(ln)
    strng=""
    #list t
    #print(b)
    t=[]
    for i in range(0,ln):
        if ciphertext[i]=='p':
            print(strng)
            t.append(int(strng))
            strng=""
        else:
            strng+=ciphertext[i]
        
    
    print(t)    
    #len()
    
    
    
    plain = [chr((char ** key) % n) for char in t]
    
    #print(plain)
    #
    
    #Return the array of bytes as a string
    return ''.join(plain)
if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print "RSA Encrypter/ Decrypter"
    keyA=RSA.generate(1024)
    #print "Generating your public/private keypairs now . . ."
    public, private = generate_keypair(11, 31)
    val=public[1]
    
    print("HELLLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOO")
    
    
    print(public)
    print(private)

    with open("in.txt","r+") as myfile:
        message = myfile.read()
   
    File=open('ExampleFile.txt','r+') 
    encrypted_msg=encrypt(val,private[0],message)
    b=list(encrypted_msg)
    print "List printed"
    print(b)
    ln=len(b)
    
    print(ln)
    
    string=""
   # print("Here"+string)
    for i in range(0,ln):
        xx=str(b[i])
       # print(xx)
        xx=xx+'p'
        print(xx)
        #print("previous"+string)
        string+=xx
        #print("Now"+string)
        #print(string)
    
    print(string)
    
    
    
    value=str(encrypted_msg)
    #rint(value)
    File.write(string)
    File.close()
    
    Again=open('ExampleFile.txt','r+')
    msg=Again.read()
    Again.close()
    #print("TRUTH OR A)
    #print(msg)
    
    #print(encrypted_msg)
    print("MESSAGE")
    print(msg)

    print "Decrypting message with our public key ",
    print "Your message is:"
    hlw= decrypt1(public, msg)
    print("Here"+hlw)
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    