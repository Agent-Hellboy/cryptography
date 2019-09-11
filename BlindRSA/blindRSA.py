import math,random

# it is an asymmetric technique used to exchange messages between two parties without meeting with each other ever   

#function to calculate modular inverse
def mod_inv(a,b):
    for i in range(1,b):
        if(a*i%b==1):
            return i

#function to calculate modular exponentiation
def mod_exp(a,b,m):
    res=1
    while(b>0):
        if(b&1):
            res=res*a%m
        a=a*a%m
        b>>=1
    return res

#function to calculate gcd of 2 number
def gcd(n,m):
    if(m==0):
        return n
    else:
        return gcd(m,n%m)


#function to calculate euler totient function known as euler phi function
def cal_phi(n):
    result=n
    for i in range(2,math.floor(math.sqrt(n))):
        if(n%i==0):
            while(n%i==0):
                n/=i
            result-=int(result/i)
    if(n>1):
        result-=int(result/n)

    return result


#function to generate the random number used for blinding the message 
def generate_rand(n):
    k=3
    t=True
    while(t==True):
        k=random.randint(1,n)
        if(gcd(n,k)==1):
            t=False
    return k




def for_signature():
    n=391
    e=2
    #(e,n) is  public key
    g=cal_phi(n)
   
    while(e<g):
        if(gcd(e,g)!=1):
            e=e+1
        else:
            break
    print("phi(n) "+str(g))
    
    k=generate_rand(n)
    print("( e ) public key for encryption "+str(e))
    m=int(input("enter the message for signature"))
    m1=mod_exp(k,e,n)
    m=m%n
    mstar=(m1*m)%n
    print("random number generated k used for masking (blinding) the message "+str(k))
    print("blinded message "+str(mstar))

    return mstar,e,k,n





def signature():
    l,e,k,n=for_signature()
    d=1
    g=g=cal_phi(n)
    for i in range(1,g):
        if(e*i%g==1):
            d=i

    m1=mod_exp(l,d,n)  
    return m1,k,n,e
    


def verify():
    m1,k,n,e=signature()
    m1=m1%n
    s=mod_inv(k,n)  #unblinding the message 
    print("required things for verification of message masked message: random number: public key: (n) and masked message",m1,k,n,s)
    sp=s*m1%n
    s1=mod_exp(sp,e,n)   #verification of message
    print("retrived message is "+str(s1))



verify()
