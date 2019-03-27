
# coding: utf-8

# In[ ]:


DATA FLOW DIAGRAM OF ALGORITHM



# ![Annotation%202019-03-28%20004514.png](attachment:Annotation%202019-03-28%20004514.png)

# ![Annotation%202019-03-28%20004551.png](attachment:Annotation%202019-03-28%20004551.png)

# In[15]:


def get_bin(x, n=0):
    return format(x, 'b').zfill(n)
    
def preprocessing():
    print("enter the plain text should be greater than 64 bit")
    p=str(input())
    L=list(p[0:32])
    R=list(p[32:64])
    return L,R


PC2=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]))
PC1=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56],[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]))
P=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32],[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]))
EXP=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]))
IP=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64],[58,50,42,34,26,28,20,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]))
IPinv=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64],[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]))

def merge_swap(p,q):
    y=''
    y=q+p
    return y
    

def IPinvs(a):
    yr=[]
    for i in range(1,65):
        yr.insert(i,a[IPinv[i]-1])
    return yr    
    

def left_circular_shift(C,a):
    for i in range(28):
        C[i]=C[(i+a)%28]    
    return C    
        
        
def PC2a(a):
    pl=[]
    for i in range(1,49):
        pl.insert(i,a[PC2[i]-1])
    return pl    
       
        
def PC1a(a):
    hr=[]
    for i in range(1,57):
        hr.insert(i,a[PC1[i]-1])
    return hr   

print("enter the key which should be greater than 64 bit")
key=str(input())
ht=PC1a(key)

def key_generator():
    C=list(ht[0:28])
    D=list(ht[28:56])
    t=''
    g=left_circular_shift(C,1)
    h=left_circular_shift(D,1)
    #print("g:",g)
    #print("h:",h)
    t=g+h
    k=PC2a(t)
    return k    
    
def permutation_function(s):
    f1=[]
    for i in range(1,33):
        f1.insert(i,s[P[i]-1])     
    return f1   

    
def expension_function(a):
    e1=[]
    for i in range(1,49):
        e1.insert(i,a[EXP[i]-1])
    return e1    
      
def Xor(a,k,l):
   
    xr=[]
    for i in range(l):
        xr.insert(i,int(a[i])^int(k[i]))     
    return xr
    
def s_box(jt):
    #conversion of 6 bit to 4 bit using a lookup table
    gh=''
    Sbox=[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    i=0
    while(i<48):
        t=[]
        t=jt[i:i+6]
        p1=''
        p2=''
        for j in range(6):
            if(j==0 or j%5==0):
                p1=p1+str(t[j])
            else:
                p2=p2+str(t[j])      
        i=i+6         
        f=Sbox[int(p1,2)][int(p2,2)]
        gh=gh+get_bin(f,4) 
    return gh 


def function(a):
    qu=key_generator()
    #print("qu:",qu,len(qu))
    l=expension_function(a)
    #print("l:",l,len(l))
    ty=Xor(l,qu,48)
    s=s_box(ty)
    p=permutation_function(ty)
    #print("p:",p)
    return p
    
            
def DES_encryption():
    L,R=preprocessing()
    
    #print("R:",R)
    round1=dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]))
    for i in range(16):
        L=R
        T=function(R)
        R=Xor(L,T,32)     
    s=merge_swap(L,R)    
    gt=IPinvs(s)    
    return gt


    
f=DES_encryption()
print("the decrypted cypher text is: ",str(f))

