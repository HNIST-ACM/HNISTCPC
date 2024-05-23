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
	for(int i=1;i<=45;i++)
    {
        n=myRand(1,1e5);
        if(i>=40)
        {
            n=1e5;
        }
        cout<<n<<endl;
        for(int j=1;j<=n;j++)
        {
            if(i==45)
            {
                cout<<i<<" ";
                continue;
            }
            else if(i==44)
            {
                cout<<83160<<" ";
                continue;
            }
            cout<<myRand(1,1e5)<<" ";
        }
        cout<<endl;
        cout<<endl;
    }
	return 0;
}
