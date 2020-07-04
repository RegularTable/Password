import hashlib 
import random

print('Enter phrase pass')

Enter=input()
mdp=[]
for a in Enter.split():
	Actual=a
	for i in list(Actual):
		Number=ord(i)-ord('a')
		if int(Number)%3==0: Actual=hashlib.sha1(Actual.encode()).hexdigest()
		if int(Number)%3==1: Actual=hashlib.sha256(Actual.encode()).hexdigest()
		if int(Number)%3==2: Actual=hashlib.md5(Actual.encode()).hexdigest()
	encode=hashlib.sha512(Actual.encode())
	mdp.append(encode.hexdigest())
	
Password=''.join(mdp)
Password=list(Password)
for i in range(0,len(Password),len(Enter)):
	Password[i]=str(chr((ord(Password[i])-33+len(Enter))%91+33))	
Password=''.join(Password)
print("\nMdp={0}  de len= {1} ".format((Password),len(Password)))
