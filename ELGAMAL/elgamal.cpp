#include<bits/stdc++.h>

using namespace std;

int n;
int sc,beta,alpha=2;
int k=853;
int c,d;


int mod_exp(int a,int b,int m)
{   int res=1;
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
int mod_inv(int a,int c){
    a = a%c;
    for(int i=1;i<c;i++){
        if ((a*i) % c == 1)
            return i;
    }
    }


void key_generation(){
    cout<<"enter size of zp"<<endl;
    cin>>n;
    cout<<"enter private key"<<endl;
    cin>>sc;
    beta=mod_exp(alpha,sc,n);
}

void encryption(){
    cout<<"enter plain text"<<endl;
    int p;
    cin>>p;
    c=mod_exp(alpha,k,n);
    int in=mod_exp(beta,k,n);
    d=in*p%n;

    cout<<"the corresponding cypher text is "<<c<<"  "<<d<<endl;

}
void decryption(){
   int ch1=mod_exp(c,sc,n);
   int ch2=mod_inv(ch1,n);
   int ans=d*ch2%n;
   cout<<"the  retrieved plain text is"<<endl;
   cout<<ans;

}

void elgamal(){
key_generation();
encryption();
decryption();
}

int main()
{
  elgamal();

  return 0;
}
