




def subset_sum(s,a,n):
    x=[]
    for i in reversed(a):
        if(s>=i):
            s=s-i
            x.append(1)
        else:
            x.append(0)       
    if(s==0):
        print("their is a solution")
    else:
        print("their is no solution") 
        
    return x                 

def mod_inv(a,c):
    a = a%c; 
    for x in range(1,c):
        if ((a*x) % c == 1): 
            return x;  
        
        
#def a1_generator():       


#def choose_w():


def setup():
    channel=[]
    a1=[2,5,9,21,45,103,215,450,946]
    channel.append(a1)
    m=2003
    channel.append(m)
    #
    w=1289
    channel.append(w)
    return channel
    
def knapsack():
    channel=setup()
    a=[i*channel[2]%channel[1] for i in channel[0]] 
    print(a)
    print("enter 9 bit binary number")    
    p=list(input())
    s=0
    i=0
    while(i<9):
        s=s+int(int(p[i])*a[i])
        i=i+1
    channel.append(s)  
    dummy=mod_inv(channel[2],channel[1])
    sbar=dummy*channel[3]%channel[1]
    g=subset_sum(sbar,channel[0],len(channel[0]))  
    print(list(reversed(g)))
    
knapsack()    
 

