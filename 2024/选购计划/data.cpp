#include<bits/stdc++.h>
#include<fstream>
#include<random>

using namespace std;

#define endl '\n'
#define PII pair<int,int>
#define F(i,a,b) for(register int i=a;i<=b;++i)
#define PLL pair<long long,long long>
#define lowbit(x) (x&(-x))

mt19937_64 rng(random_device{}());
long long myRand(long long l,long long r) {
    uniform_int_distribution<long long> uid(l,r);
    return uid(rng);
}

const int key=5;
const int N=2e6+10;
const long long INF=(1ll<<60);
const long long inf=(1ll<<30);
const int mod=1e9+7;

int n,m,V;

int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	for(int i=1;i<=145;i++)
    {
        n=myRand(1,5000);m=myRand(1,5000);V=myRand(1,5000);
        
        if(i>=30)
        {
            n=myRand(4000,5000);
            m=myRand(4000,5000);
            V=myRand(4000,5000);
        }
        if(i>=41)
        {
            n=5000;m=5000;V=5000;
        }
        if(i>=46)
        {
        	n=myRand(5,20);
        	m=myRand(1,20);
        	V=20;
		}
        cout<<n<<" "<<m<<" "<<V<<endl;
        for(int j=1;j<=n;j++)
        {
            if(i==41)
            {
                cout<<1<<endl;
                continue;
            }
            else if(i==42)
            {
                cout<<2000<<endl;
                continue;
            }
            else if(i==43)
            {
                cout<<4000<<endl;
                continue;
            }
            else if(i==44)
            {
                cout<<2500<<endl;
                continue;
            }
            else if(i==45)
            {
                cout<<5000<<endl;
                continue;
            }
            
            int x=myRand(1,5000);
			if(i>=46)
            {
            	x=myRand(1,10);
			}
            cout<<x<<endl;
        }
        cout<<endl;
    }
	return 0;
}
