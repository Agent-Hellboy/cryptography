#k=(n,p,q,m)
#db=(p,q)
#eb=(n,m)
#m is an element of zn*

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
    
def setup():
    print("enter two distinct prime number should be of the form p,q=3(mod4) :prefered one is 7 and 11")
    p=int(input())
    q=int(input())         
    n=p*q
    return p,q,n    
        
def encryption():
    p,q,n=setup()
    c=[]
    print("enter plain text in binary:")
    P=list(input())
    y=2
    while(y<n):
        if(gcd(y,n)!=1):
            y=y+1 
        else:
            break
    m=6
    print(m**((p-1)/2)%p)
    print(m**((q-1)/2)%q)
    for i in range(len(P)):
        c1=(m**int(P[i])*y**2)%n
        c.append(c1)
    
    print("the encrypted cypher text is:")
    print(c)
    return c,p,q 
    
                
def decryption():
    y,p,q=encryption()
    s=[]
    for i in range(len(y)):
        if(int(y[i])**((p-1)/2)%p==1 and int(y[i])**((q-1)/2)%q==1):
            s.append(0)
        else:
            s.append(1) 
    print("the retrived plain text is")
    print(s)
    
    
def goldwasser_micali():
    decryption()
    
goldwasser_micali()    
