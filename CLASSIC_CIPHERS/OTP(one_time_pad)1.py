from random import randint

def convert_to_bits(n,pad):
	result=[]
	while(n>0):
		if(n%2==0):
			result=[0]+result
		if(n%2!=0):
			result=[1]+result
		n=n//2
	while(len(result)<pad):
		result=[0]+result
	return result


#print(convert_to_bits(10,6))

def strings_to_bits(s,pad):
	result=[]
	for c in s:
		result=convert_to_bits(ord(c),pad)+result
	return result


def bits_to_string(s,pad):
	string=''
	for i in range(len(s)//pad):
		num=0
		k=0
		lis=reversed(s[i*pad:(i+1)*pad])
		for j in lis:
			num=num+j*pow(2,k)
			k+=1
		string=chr(num)+string
	return string

#print(strings_to_bits('CS',7))


def generate_rand(length):
	global key
	k=[]
	while(len(k)<length):
		l=randint(10,18)
		k=convert_to_bits(l,0)+k
	key=k[:length]
	return key

def encrypt():
	global pad
	pad=7
	m=input("enter message to encrypt")
	plain_text=strings_to_bits(m,pad)
	mes=strings_to_bits(m,pad)
	key=generate_rand(len(mes))
	cipher=[me^ke for me,ke in zip(mes,key)]
	plain_cipher=bits_to_string(cipher,pad)
	print('the cipher text of given input {} which in binary form is {} is {} which in binary form is {}'.format(m,plain_text,plain_cipher,cipher))
	return cipher



def decrypt():
	cipher=encrypt()
	plain_text=[me^ke for me,ke in zip(cipher,key)]
	out=bits_to_string(plain_text,pad)
	print(out)
	return out


def options(argument):
	if(argument==1):
		s=str(input("do you wants to decrypt also"))
		if(s=='YES'):
			decrypt()
		else:
			print("your encrypted message is :\n")
			encrypt()
	if(argument==2):
		decrypt()
 
if __name__ == "__main__": 
	while(True):
	    print("choose from following\n1.encrypt\n2.-----")
	    l=int(input())
	    if(l==3):
	    	break
	    options(l)

    
