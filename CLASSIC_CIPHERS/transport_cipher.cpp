#include <bits/stdc++.h>
#include <list>
using namespace std;
list<char>v[2];
list<char>rt;
list<char>::iterator it;
void encryption(){
    cout<<"enter the plain text to decrypt:"<<endl;
    string s;
      cin>>s;
      int j=0;
      while(j<s.length()){
        if(j%2==0){
          v[0].push_back(s[j]);
        }
        else
         v[1].push_back(s[j]);
          j++;

      }
      cout<<"the encrypted cipher text is:";

      for(it=v[0].begin();it!=v[0].end();it++)
      {
          cout<<*it;
      }
      for(it=v[1].begin();it!=v[1].end();it++)
      {
          cout<<*it;
      }
      cout<<endl;

}

void decryption()
{
    while(!v[0].empty())
      {
          rt.push_back(v[0].front());
          rt.push_back(v[1].front());
          v[0].pop_front();
          v[1].pop_front();
      }
      cout<<"the plain text retrieved from cipher text is:";
      for(it=rt.begin();it!=rt.end();it++)
      {
          cout<<*it;
      }
      cout<<endl;
}

void transport_cipher()
{
    encryption();
    decryption();
}
int main(){
      transport_cipher();
      return 0;

}

