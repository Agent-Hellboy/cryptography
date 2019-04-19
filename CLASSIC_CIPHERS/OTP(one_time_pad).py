

import random
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def preprocessing(a):
    l=[]
    while(a>0):
        l.append(random.randint(0,26))
        a=a-1
    a1=dict(zip(l1,l2))
    g=dict((l2, l1) for l1, l2 in a1.items())
    return a1,g,l

def encryption():
    print("enter the input to encrypt")
    p=input(list)
    le=len(p)
    a1,g,l=preprocessing(le)
    t=[]
    for i in range(0,le):
        t.append(g[((a1[p[i]]+l[i])%26)])
    print("the cipher text generated is:")
    print(t)
    return t,l,a1,g

def decryption():
    t,l,a1,g=encryption()
    le=len(l)
    ou = []
    for i in range(0,le):
        ou.append(g[(a1[t[i]]-l[i])%26])

    print("the retrived plain text is:")
    print(ou)

decryption()

