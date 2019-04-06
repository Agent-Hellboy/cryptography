import math as m
key=[3,10,9,4,13,6,3,15]

def get_bin(x, n=0):
    return format(x, 'b').zfill(n)



def key_generation():
    k=[]
    for i in key:
        k.append(get_bin(i,4))
    return k    



def encryption():
    y=key_generation()
    cipher=[]
    print("enter the plain text in binary :")
    s=str(input())
    g=len(s)
    #print("before:",s,len(s))
    t=g%4
    t=4-t
    while(t>0):
        s=s+'0'
        t=t-1 
    Aflen=len(s)    
    #print("after:",s,len(s))    
    j=0
    z=0
    t=0
    while(z<len(s)):
        g=''
        for i in range(4):
                g=g+s[j]
                j=j+1
        l=int(g,2)
        #print(l)
        cipher.insert(t,l^int(y[t],2))
        t=t+1
        z=z+4
    return cipher,Aflen   


def decryption():
    t=key_generation()
    s,k=encryption()
    #print(s,k)
    cip=''
    d=0
    while(d<len(s)):
        cip=cip+str(get_bin(s[d],4))
        d=d+1
    print("the cipher text generated is:")    
    print(cip)
    Rplain=[]
    v=''
    for i in range(k//4):
        Rplain.insert(i,s[i]^int(t[i],2))
        v=v+str(get_bin(Rplain[i],4)) 
        
    print("the retrived plain text is:")
    print(v)    
    
def stream_cipher():
    decryption()
    
stream_cipher()    
