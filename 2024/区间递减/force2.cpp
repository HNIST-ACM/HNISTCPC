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
int n,q;
int a[N];
int b[N], m;

int solve(int l, int r) {
    m = r-l+1;
    memcpy(b, a+l, sizeof(int)*m);
    while(!is_sorted(b, b+m, greater<>())) {
        int i=0;
        for(; i+1<m; ++i) {
            if(b[i]>b[i+1]) {
                break;
            }
        }
        while(i+1 < m) {
            b[i] = b[i+1];
            i++;
        }
        m--;
    }
    return m;
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin>>n>>q;
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
            else flag=1, cout<<(ans=r-l+1-solve(l,r))<<"\n";
            continue;
        }
        cout<<r-l+1-solve(l,r)<<"\n";
    }
    return 0;
}
/*




*/