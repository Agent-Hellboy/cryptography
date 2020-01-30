
#function to find modular exponent
def mod_mul(h,l,p):
    res=1
    while(l>0):
        if(l&1):
            res=res*h%p
        h=h*h%p
        l>>=1
    return res

#function to find modular inverse
def mod_inv(a,b):
    for i in range(1,b):
        if(a*i%b==1):
            return i



def setup():
    print("enter value of prime p and q where q must divides p-1")
    p=int(input())
    q=int(input())
    h=2
    g=mod_mul(h,int((p-1)/q),p)
    print("enter a random integer which is a generator of class Zp*")
    x=int(input())
    y=mod_mul(g,x,p)
    return g,x,p,q,y


def signing():
    g,x,p,q,y=setup()
    print("enter message to sign")
    m=int(input())
    print("enter a random integer which is ephimeral key")
    k=int(input())
    rp=mod_mul(g,k,p)
    r=rp%q
    sp=mod_inv(k,q)
    s=sp*(m+r*x)%q
    return r,s,y,q,m,g,p



def verifying():
    r,s,y,q,m,g,p=signing()
    w=mod_inv(s,q)
    u1=m*w%q
    u2=r*w%q
    vp=mod_mul(g,u1,p)
    vpp=mod_mul(y,u2,p)
    v=((vp*vpp)%p)%q
    print(v,r)
    if(v==r):
        print("message verified")


def DSA():
    verifying()
 
 
DSA()
