#include <bits/stdc++.h>
//rabin cryptosystem based on the fact that factorization is hard
using namespace std;
int d,yp,yq;

int mod_exp(int a,int b,int m)
{
    int res=1;
    while(b>0)
    {
        if(b&1){
            res=res*a%m;
        }
        a=a*a%m;
        b>>=1;
    }
    return res;
}

void extended_eulid(int a,int b)
{
    if(b==0)
    {
        d=a;
        yp=1;
        yq=0;
    }
    else
    {
        extended_eulid(b,a%b);
        int temp=yp;
        yp=yq;
        yq=temp-(a/b)*yq;
    }
}
int p,q,n,c;

void key_generation()
{
    cout<<"enter 2 prime number of the form 3=p%4 and 3=q%4"<<endl;
    p,q;
    cin>>p>>q;
    n=p*q;

}

void encryption()
{
    cout<<"enter the plain which must be smaller than "<<n<<endl;
    int m;
    cin>>m;
    c=m*m%n;
    cout<<"cipher text is:"<<c<<endl;
}

void decryption()
{

    int r,s,mp,mq;

    extended_eulid(p,q);
    //cout<<"yp: "<<yp<<"yq: "<<yq<<endl;
    mp=mod_exp(c,(int)((p+1)/4),p);
    mq=mod_exp(c,(int)((q+1)/4),q);
    //cout<<"mp: "<<mp<<"mq: "<<mq<<endl;
    r=abs((yp*p*mq+yq*q*mp)%n);

    s=abs((yp*p*mq-yq*q*mp)%n);


    cout<<"the possible plain text where after decryption "<<endl;
    cout<<r<<" "<<n-r<<"  "<<s<<"  "<<n-s;


}
 void rabin()
 {
     key_generation();
     encryption();
     decryption();
 }

int main()
{


   rabin();

   return 0;
}
