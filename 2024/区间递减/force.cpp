#include<iostream>
#include<cmath>
#include<cstring>
#include<cassert>
#include<string>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<unordered_map>
#include<map>
#include<vector>
#include<set>
#include<unordered_set>
#include<bitset>
#include<climits>
#include<numeric>
#include<functional>
#include<iomanip>
#include<list>
#ifdef YJL
#include<debug.h>
#else
#define debug(args...)0
#define debug_n(a,n)0
#endif
#define ALL(a) a.begin(),a.end()
using namespace std;
using ll=long long;

constexpr int N = 2e5 + 10;

int solve(list<int>&& a) {
    auto it=a.begin();
    while(!is_sorted(ALL(a),greater<>())) {
        while(next(it)!=a.end() and *it<=*next(it))
            it++;
        it=a.erase(it);
        if(it!=a.begin())
            --it;
    }
    return a.size();
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    int n,q;
    cin>>n>>q;

    vector<int> a(n);
    for(int i=0; i<n; ++i) {
        cin>>a[i];
    }
    int flag=0, ans=0;
    while(q--) {
        int l,r;
        cin>>l>>r;
        --l,--r;
        if(l==0 and r==n-1) {
            if(flag) cout<<ans<<"\n";
            else flag=1, cout<<(ans=r-l+1-solve(list(a.begin()+l, a.begin()+r+1)))<<"\n";
            continue;
        }
        cout<<r-l+1-solve(list(a.begin()+l, a.begin()+r+1))<<"\n";
    }
    return 0;
}
/*




*/