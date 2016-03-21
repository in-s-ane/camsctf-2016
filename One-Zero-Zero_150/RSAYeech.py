#!/usr/bin/python

import sys;

k = 40634905927881125837687153L #int("0x219cc6aa0ec13d041c4971",16);
totient = 40634905927850661848135028L;
c = 13016925875285007045101206L;

# Assume ethan was right, in that cipher is indeed e, that makes k the mod
# So d is the modular inverse of c over k

def gcd(a,b): # Euclidean Algorithm
	while a:
		a, b = b%a, a;
	return b;

def egcd(a,b): # Extended Euclidean Algorithm
	if a == 0:
		return (b,0,1);
	else:
		g,y,x = egcd(b%a,a);
		return (g, x - (b // a) * y, y);

def modinv(a,m): # Modular Inverse Finder
	g, x, y = egcd(a,m);
	if g != 1:
		raise Exception('modular inverse does not exist');
	else:
		return x % m;

def printableAscii(string):
	charList = list(string);
	for el in string:
		if ord(el) < 32 or ord(el) > 126:
			return False;
	return True;
n = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
e = 65537
d = 27856072577004096911396713846850363584417408026591016459417310603194644749492416868137791178719126

c = 202915876039746229935722670340487424839857163073658749653272992778826868242273898753310832920993983342

f = open('data2', 'r').read().split('\n')[:-1]

string = ""

for c in f:
    c = int(c)
    m = pow(c, d, n)
    hexM = hex(m)
    if len(str(hexM[2:-1])) % 2 == 0:
        string += hexM[2:-1].decode('hex');
        print hexM[2:-1].decode('hex')
    else:
        string += (hexM[2:-1] + '0').decode('hex');
        print (hexM[2:-1] + '0').decode('hex');

actual_answer = ""

for char in string:
    if not (ord(char) < 32 or ord(char) > 126):
        actual_answer += char


print actual_answer

#d = modinv(c,totient); # Doesn't make sense b/c c is not coprime to totient
#d = modinv(c/2,totient); # Makes 0 sense

#f = open("RSASolve.txt","a");
#
#for e in range(0,int(sys.argv[1])):
#	if gcd(e,totient) == 1:
#		d = modinv(e,totient);
#		m = pow(c,d,k);
#		hexM = hex(m);
#		#print "e: %d" %(e);
#		#print "d: %d" %(d);
#		#print "Hex: %s" %(hex(d));
#		if len(str(hexM)[2:-1]) % 2 == 0:
#			#f.write("\n" + str(e) + ": " + str(hexM)[2:-1].decode("hex"));
#			if printableAscii(str(hexM)[2:-1].decode("hex")):
#				print str(hexM)[2:-1].decode('hex');
#		#print "Result: %s" %(hex(d)[2:].decode("hex"));
#
#print "we done here"
#
#
##Str = hexD[2:]
##print Str.decode("hex");
