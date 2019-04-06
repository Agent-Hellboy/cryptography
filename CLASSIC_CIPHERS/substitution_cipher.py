



def setup():
    l=dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['x','n','y','a','h','p','o','g','z','q','w','b','t','s','f','l','r','c','v','m','u','e','k','j','d','i']))
    r=dict(zip(['x','n','y','a','h','p','o','g','z','q','w','b','t','s','f','l','r','c','v','m','u','e','k','j','d','i'],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))






def encryption():
    s=[]
    p=list(input())
    i=0
    while(i<len(p)):
        g=l[p[i]]
        s.append(g) 
        i=i+1
    return s       






def decryption():
    pl=[]
    e=encryption()
    print("the cipher text obtained is:")
    print(e)
    i=0
    while(i<len(e)):
        f=r[e[i]]
        pl.append(f)
        i=i+1
    print("the retrived plain text is:") 
    print(pl)

setup()

decryption()
        

